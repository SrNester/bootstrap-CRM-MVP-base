from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from .models import Lead, Company, LeadSource
from .serializers import UserSerializer, LeadSerializer, CompanySerializer, LeadSourceSerializer
from .tasks import score_lead


User = get_user_model()


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class LeadFilter(filters.FilterSet):
    email = filters.CharFilter(lookup_expr='icontains')
    score_min = filters.NumberFilter(field_name='score', lookup_expr='gte')
    score_max = filters.NumberFilter(field_name='score', lookup_expr='lte')
    
    class Meta:
        model = Lead
        fields = ['email', 'score_min', 'score_max']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrReadOnly]


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by("-created_at")
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination


class LeadSourceViewSet(viewsets.ModelViewSet):
    queryset = LeadSource.objects.all().order_by("-created_at")
    serializer_class = LeadSourceSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all().order_by("-created_at")
    serializer_class = LeadSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = LeadFilter
    
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def rescore(self, request, pk=None):
        """
        Endpoint para rescoring manual de un lead específico.
        POST /api/leads/{id}/rescore/
        """
        lead = self.get_object()
        
        try:
            # Enqueue the scoring task
            task = score_lead.delay(lead.id)
            
            return Response({
                'message': 'Rescoring task enqueued successfully',
                'task_id': task.id,
                'lead_id': lead.id
            }, status=status.HTTP_202_ACCEPTED)
            
        except Exception as e:
            return Response({
                'error': 'Failed to enqueue rescoring task',
                'details': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)