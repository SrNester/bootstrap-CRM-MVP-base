from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core.views import UserViewSet, LeadViewSet, CompanyViewSet, LeadSourceViewSet


def health(_request):
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", health),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"companies", CompanyViewSet)
router.register(r"lead-sources", LeadSourceViewSet)
router.register(r"leads", LeadViewSet)

urlpatterns += [
    path("api/", include(router.urls)),
]