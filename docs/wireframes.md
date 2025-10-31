# Wireframes — Panel CRM y Flujo de Leads (Semana 0)

> Versión inicial en texto/diagramas simples para orientar UI/UX. Se migrará a Figma posteriormente.

## 1. Panel (Listado de Leads)
- Encabezado: buscador (`email`), filtros (`score_min`, `score_max`).
- Tabla (paginada): `Nombre`, `Email`, `Teléfono`, `Score`, `Empresa`, `Fuente`, `Acciones`.
- Acciones por fila: `Ver`, `Editar`, `Rescore`.

```
-------------------------------------------------------------+
| Buscar: [    ]  Score: [min] [max]    [Filtrar]            |
-------------------------------------------------------------+
| Nombre        | Email                  | Score | Empresa    |
|-------------------------------------------------------------|
| C. Ruiz       | carlos@ex.com          | 0.7   | Tech Sol.  |
| M. Rodriguez  | maria@techsolutions... | 0.7   | Tech Sol.  |
-------------------------------------------------------------+
| « Página 1 de N »    [<] [>]   Tamaño página: 20           |
-------------------------------------------------------------+
```

## 2. Detalle de Lead
- Datos básicos: nombre, email, teléfono, empresa, fuente.
- Score + explicación IA.
- Botón `Rescore`.
- Interacciones (timeline simple).

```
[ Lead: Maria Rodriguez ]    [Rescore]
Email: maria@techsolutions.com
Tel: +34...
Empresa: Tech Solutions | Fuente: WhatsApp Campaign

Score: 0.7
Explicación: Reglas simples basadas en presencia de email/phone...

Interacciones:
- 2025-10-31 Outbound (whatsapp): "Hola Maria..."
- 2025-10-31 Inbound  (whatsapp): "Gracias..."
```

## 3. Crear Lead
- Formulario con campos: nombre, email, teléfono, `company`, `source`.
- Al guardar: se encola scoring automático.

## 4. Flujo de Leads (alto nivel)
1) Ingesta (manual/API/CSV) → 2) Normalización → 3) Scoring IA → 4) Reglas/acciones → 5) Seguimiento (interacciones/tareas).

## 5. Navegación
- `Leads`, `Companies`, `Lead Sources`, `Reports` (futuro).

## 6. Notas
- Diseño responsive, enfoque datos primero.
- En MVP no se incluyen dashboards gráficos.