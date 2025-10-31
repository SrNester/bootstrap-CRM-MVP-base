# CRM Empresarial con Automatización por IA (Email + WhatsApp)

Proyecto monorepo para construir un CRM multicanal con automatización basada en IA.

Stack principal:
- Backend: `Django` + `Django REST Framework`
- Orquestador IA: `FastAPI`
- Mensajería: `Meta WhatsApp Cloud API` / `Twilio`
- Base de datos: `PostgreSQL`
- Frontend: `Flutter` (panel y mobile app, posterior)
- Tareas asíncronas: `Celery` + `Redis`
- IA: `Mistral` o `GPT` para generación y análisis

## Estado actual (Fase 0)
- Estructura base del proyecto.
- Docker Compose con `PostgreSQL`, `Redis`, `Django` (API), `FastAPI` (IA), `Celery worker` y `Celery beat`.
- Variables de entorno de ejemplo.
- Documentación de arquitectura inicial.

## Inicio rápido

1. Crear archivo `.env` a partir de `.env.example` y ajustar valores.
2. Construir y levantar servicios:
   ```bash
   docker compose up -d --build
   ```
3. Comprobar salud:
   - Django: `http://localhost:8000/health`
   - FastAPI: `http://localhost:9000/health`

Notas:
- Asegúrate de tener Docker Desktop instalado y con `docker compose` disponible.
- En Windows, ejecuta los comandos en PowerShell o tu terminal preferida.

## Estructura del repositorio

```
backend/                # Django + DRF + Celery (worker/beat)
ai_orchestrator/        # FastAPI para scoring y generación IA
docs/                   # Documentación técnica
docker-compose.yml      # Orquestación de servicios
.env.example            # Variables de entorno de ejemplo
README.md               # Este archivo
```

## Siguientes pasos
- Semana 1: modelos base (`User`, `Company`, `Lead`, `Interaction`, `AutomationRule`, `Task`), autenticación JWT y CRUD de usuarios/leads.
- Semana 2: ingesta de leads (CSV y formularios) y normalización/validación.
- Semana 3: scoring de leads automático vía IA.