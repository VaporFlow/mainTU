# TRD – Módulo Checks Forecast – MainTU

## 1. 🔄 Descripción General

El módulo **Checks Forecast** de MainTU se encarga de **analizar eventos de chequeos programados** y agruparlos según restricciones configurables como disponibilidad de slots, tareas combinables, y mano de obra. A partir de los archivos de forecast exportados de AMOS, se genera una visualización tabular del volumen de chequeos a realizar por tipo y ventana temporal, así como una tabla editable de agrupaciones recomendadas.

---

## 2. ⚖️ Alcance Funcional

### Funciones principales:
- Cargar y analizar archivos CSV con eventos de chequeo (`Forecast_<timestamp>.csv`).
- Normalizar columnas, mapear eventos a chequeos conocidos.
- Calcular cantidad de chequeos por tipo en ventanas de 1, 2, 3, 6 y 12 meses.
- Asociar a cada tipo de chequeo los recursos requeridos (slots, personal).
- Sugerir agrupaciones optimizadas según restricciones configurables.
- Permitir edición manual de agrupaciones por el usuario.
- Mostrar resultados tanto en **tabla** como en **Gantt interactivo**.
- Exportar resultados a Excel.

---

## 3. 🌐 Arquitectura

### Backend (Django):
- App: `checks_forecast`
- Modelos:
  - `CheckForecastWindow`
  - `CheckRequirement` (relaciona tipo de chequeo con partes/personal)
  - `CheckGroup` (agrupación sugerida por ventana)
- Tareas:
  - Procesar archivo forecast y mapear eventos a chequeos.
  - Agrupar eventos en ventanas de tiempo (DateOffset).
  - Calcular requerimientos por agrupación.

### Frontend (React):
- Vista `/checks-forecast`
- Componentes:
  - Tabla resumen por tipo de chequeo
  - Tabla de agrupaciones sugeridas
  - **Gantt** de programación por semana/base
  - Botón de "Reanalizar" / "Exportar"

---

## 4. 💡 Lógica de Agrupación

- Para cada fila de `Forecast_<timestamp>.csv`, se extrae:
  - `Event/Description`, `Expected`, `AC Reg`
- Se mapea el evento a un tipo de chequeo según `mapping` definido en admin
- Se agrupa por `Check` y por ventana temporal según `Expected`
- Se suma la cantidad total por tipo de chequeo por ventana
- A cada tipo de chequeo se le asocian sus requisitos (slots, partes, personal)
- Se propone una tabla de agrupación por semana con asignación óptima

---

## 5. 📊 Tablas Relevantes

### Tabla Forecast Agrupado (renderizada en frontend)
| Check | 1mo | 2mo | 3mo | 6mo | 12mo |
|-------|-----|-----|-----|------|------|
| IC01  |  3  |  5  |  9  |  12  | 15   |

### Tabla Agrupaciones Recomendadas
| Semana | Base | Chequeos agrupados | Slot requerido | Personal estimado |
|--------|------|---------------------|----------------|-------------------|
| W30/25 | AEP  | IC01, IC02          |     2          |        5          |

### Gantt (visualización)
- Eje X: semanas del año
- Eje Y: AC Reg o agrupación
- Cada bloque representa un grupo de chequeos asignados a un slot/base en determinada semana

---

## 6. 🎓 Reglas de Negocio

- Cada evento puede ser mapeado a un solo tipo de chequeo
- Si no hay mapping, el evento se descarta del cálculo
- Las agrupaciones deben respetar:
  - Cantidad máxima de slots por semana y base (configurable)
  - Tareas no combinables se asignan a slots separados
- Las restricciones se configuran desde Django Admin

---

## 7. ⚡ Entrada y Salida

### Entrada esperada:
Archivo `Forecast_<timestamp>.csv` con al menos columnas:
- `Event/Description`
- `Expected`
- `AC Reg`

### Salida:
- DataFrame/tablas agrupadas renderizadas en frontend
- Gantt interactivo por agrupación y semana
- Archivo Excel con:
  - Hoja "Forecast por chequeo"
  - Hoja "Agrupaciones recomendadas"

---

## 8. 🚀 Consideraciones de Escalabilidad

- Las ventanas de tiempo deben poder modificarse sin tocar código
- El mapping evento → chequeo debe ser editable desde admin
- Las agrupaciones sugeridas pueden reoptimizarse tras edición de restricciones
- El Gantt debe soportar zoom y filtros por base, tipo o rango de fecha

---

## 9. 🌍 Endpoints API (DRF)

- `POST /api/checks-forecast/analyze/` → analiza archivo forecast cargado
- `GET /api/checks-forecast/summary/` → devuelve forecast por ventana
- `GET /api/checks-forecast/groups/` → devuelve agrupaciones sugeridas
- `GET /api/checks-forecast/gantt/` → devuelve datos para renderizar Gantt
- `POST /api/checks-forecast/export/` → exporta resultado a Excel

---

