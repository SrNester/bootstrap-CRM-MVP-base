# Documento de Requerimientos (PRD) — MVP CRM Multicanal

## 1. Objetivo
- Construir un CRM básico multicanal (Email + WhatsApp) que permita registrar leads, evaluar su potencial con scoring IA y ejecutar acciones simples.

## 2. Alcance (MVP)
- Gestión de entidades: `Company`, `LeadSource`, `Lead`.
- Autenticación JWT para proteger la API.
- CRUD de leads con filtros y paginación.
- Scoring automático de leads vía Celery + FastAPI.
- Registro de interacciones (email/whatsapp) manuales en esta fase.
- Endpoint para rescoring manual.

Fuera de alcance (MVP): frontend en Flutter, integraciones reales de envío (Twilio/Meta), dashboards.

## 3. Requerimientos funcionales
- RF1: Crear/listar/filtrar leads por `email` y rango de `score`.
- RF2: Crear `Company` y `LeadSource` y asociarlas a leads.
- RF3: Disparar scoring automático al crear/actualizar lead (cuando aplique).
- RF4: Permitir rescoring manual (`POST /api/leads/{id}/rescore`).
- RF5: Registrar interacciones (`Interaction`) con canal `email` o `whatsapp` (entrada mínima: lead, mensaje, dirección).

## 4. Requerimientos no funcionales
- RNF1: Orquestación en Docker Compose (PostgreSQL, Redis, Django, FastAPI, Celery worker/beat).
- RNF2: Configuración vía `.env` y secretos locales.
- RNF3: Logs claros en worker Celery.

## 5. API (resumen)
- `POST /api/token/` (JWT) y `POST /api/token/refresh/`.
- `/api/leads/` CRUD + filtros (`email`, `score_min`, `score_max`) + paginación.
- `/api/leads/{id}/rescore/` acción.
- `/api/companies/` CRUD.
- `/api/lead-sources/` CRUD.

## 6. Flujos clave
- Ingesta: crear lead (opcionalmente asignar `company` y `source`).
- Scoring: publicar tarea Celery, FastAPI devuelve score y explicación, persistir en Django.
- WhatsApp: uso básico como fuente (`LeadSource`), sin envío real en MVP.

## 7. Criterios de aceptación
- CA1: `docker compose up` levanta todos los servicios; health ok en Django.
- CA2: CRUD de `leads`, `companies`, `lead-sources` funcional con JWT.
- CA3: Scoring automático probado y logs en worker confirman ejecución.
- CA4: Filtros y paginación devuelven resultados consistentes.

## 8. Métricas iniciales (opcionales)
- Nº de leads creados, % con score > 0.5, nº interacciones por canal.