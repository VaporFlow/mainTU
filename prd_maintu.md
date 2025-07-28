# PRD – MainTU: Plataforma de Forecast y Programación de Mantenimiento

## 1. 📌 Resumen Ejecutivo

**MainTU** es una aplicación web full stack orientada a equipos de planificación y mantenimiento aeronáutico. Su objetivo es automatizar la previsión de partes y programación de chequeos de flotas mediante el procesamiento de archivos exportados desde AMOS. Presenta resultados claros, visuales y exportables para la toma de decisiones.

La plataforma es modular, extensible y segura. Opera en un entorno Dockerizado desplegado sobre Ubuntu (Vultr). Cada módulo aborda una necesidad específica de la planificación técnica.

---

## 2. 🌟 Objetivos

- Automatizar el análisis de partes y chequeos a partir de archivos AMOS.
- Visualizar alertas por faltantes o consumo anticipado.
- Agrupar tareas según restricciones de slots, personal y chequeos compatibles.
- Asignar tareas a sectores (Línea o Menor) y permitir confirmar ejecuciones.
- Escalar a múltiples flotas, roles y escenarios simulados (“what-if”).

---

## 3. 🧑‍💼 Alcance MVP

### Incluido:

- Subida y renombrado de archivos CSV desde interfaz.
- Detección de tipo de archivo según contenido (no sólo nombre).
- Análisis Parts Forecast: consumo, stock y alertas por ventana.
- Visualización de forecast y tabla con partes requeridas.
- Django Admin: usuarios, mappings y requisitos por chequeo.

### Excluido:

- Checks Forecast (se desarrollará posterior).
- Exportación PDF o integración con AMOS online.

---

## 4. 🔄 Módulos

### 1. Parts Forecast

- Ingesta de CSV: detecta según columnas como "AEP Qty", "EZE Qty" o "Event/Description".
- Renombrado automático: `AEP_<timestamp>.csv`, `EZE_<timestamp>.csv`, `Forecast_<timestamp>.csv`.
- Mapeo evento → chequeo.
- Cálculo de partes requeridas por ventana: 1, 2, 3, 6, 12 meses.
- Comparativa contra stock (AEP + EZE).
- Exportación de tabla de forecast a Excel.

### 2. Checks Forecast *(futuro)*

- Agrupación por fechas esperadas.
- Reglas configurables desde admin:
  - Slots disponibles (por base)
  - Tareas compatibles
  - Disponibilidad de personal
- Forecast por chequeo y bloque de programación sugerido
- Tabla editable de agrupaciones
- Exportación a Excel

### 3. Maintenance Programming *(futuro)*

- Asignación diaria de tareas por sector
- Confirmación de ejecución
- Reportes de cumplimiento y causas de desvío

### 4. Usuarios y Roles

- Login local con email/contraseña.
- Roles:
  - Compras: sólo Parts Forecast.
  - CCM: todos los módulos, programación y escenarios.
  - Mantenimiento: tareas asignadas y confirmación.

### 5. Escenarios y Multiflota *(futuro)*

- Clonar y aplicar escenarios what-if.
- Dashboard por flota.

---

## 5. 📊 KPIs Iniciales

| Métrica                          | Valor Objetivo |
| -------------------------------- | -------------- |
| Tiempo desde subida a forecast   | < 10 segundos  |
| Errores en detección de tipo CSV | 0              |
| Alertas por partes faltantes     | 100% precisión |

---

## 6. 📅 Requisitos Técnicos

- Backend: Django + DRF
- Frontend: React (SPA) + MUI
- DB: PostgreSQL
- Infraestructura: Docker Compose (backend, frontend, db, media/static)
- Seguridad: login local, CORS, CSRF, .env, roles
- Lógica de renombrado basada en lectura de cabeceras del CSV

---

## 7. 🎓 Reglas de Negocio

- Si un CSV contiene "AEP Qty" → se renombra como `AEP_<timestamp>.csv`
- Si contiene "EZE Qty" → `EZE_<timestamp>.csv`
- Si contiene "Event/Description" → `Forecast_<timestamp>.csv`
- Un mismo chequeo puede requerir múltiples partes
- El consumo se calcula multiplicando la cantidad requerida por chequeo por la cantidad de chequeos programados
- Forecast agrupa tareas por mes desde la fecha actual

---

## 8. 🚡 No Funcional

- El sistema debe estar dockerizado y ser desplegable en servidores Vultr
- Soporta carga de múltiples archivos sin bloqueo
- Arquitectura preparada para escalar por módulo y rol

---

## 9. 🏃‍ Restricciones

- Los archivos deben venir desde AMOS y respetar su estructura esperada
- No se permite el uso de Microsoft Entra ID para autenticación
- El sistema puede compartir servidor con otras apps
- No se procesan archivos sin cabecera reconocible

---

## 10. 📂 Estructura de Proyecto (Resumen)

```
MainTU/
├── backend/
│   ├── parts_forecast/
│   ├── checks_forecast/
│   └── maintu/ (core)
├── frontend/
├── docker-compose.yml
├── .env.example
```

---

