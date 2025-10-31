# Arquitectura Técnica — CRM IA Multicanal

## Visión general
Sistema CRM con automatización inteligente y multicanal (Email + WhatsApp) organizado como monorepo con microservicio de IA.

## Componentes
- Backend (API): Django + DRF
- Orquestador IA: FastAPI (scoring y generación de contenido)
- DB: PostgreSQL
- Cache/Cola: Redis
- Tareas: Celery (worker + beat)
- Frontend: Flutter (panel y mobile) — a implementar en semanas posteriores

## Comunicación
- Django → FastAPI vía `HTTP` (`AI_SERVICE_URL`)
- Celery usa `Redis` como broker y backend

## Despliegue local
- `docker-compose` orquesta servicios
- Variables de entorno en `.env`

## Seguridad y autenticación
- JWT en Django (*pendiente* en Semana 1)
- Permisos/roles avanzados (*Semana 11*)

## Flujos clave (MVP)
1. Ingesta de leads (CSV y formularios)
2. Scoring de leads vía IA y reglas simples
3. Automatizaciones internas (asignación, tareas, borradores de email)
4. Envío de Email (aprobación previa) y mensajes WhatsApp (integración básica)

## Métricas y reportes
- Endpoints en Django para KPIs de canales
- Dashboards en Flutter/React con gráficas

## Operación
- Worker Celery para procesamiento de eventos/leads
- Beat Celery para tareas programadas (ej. reporte semanal)