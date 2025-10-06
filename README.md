#  Proyecto ETL + API + Dashboard - Gestión de Ventas Grupo ATLAS

Este proyecto implementa una **mini aplicación completa de gestión de ventas**, con integración entre bases de datos MySQL, un backend en Flask, un frontend responsivo con Bootstrap y un dashboard analítico en Power BI.

---

## Estructura del Proyecto

---

## Descripción Técnica

### Bases de Datos

El sistema utiliza dos bases MySQL:
- **base_envio** → Base de datos **fuente**, donde se registran clientes, productos y ventas.
- **base_cargue** → Base de datos **destino**, actualizada mediante un proceso **ETL**.

Tablas principales:
- `clientes (id_cliente, nombre, correo, ... )`
- `productos (id_producto, nombre, categoria, precio, ... )`
- `ventas (id_venta, id_cliente, id_producto, cantidad, fecha_venta, ...)`

---

### Backend (Flask)

El backend está dividido en dos módulos:
1. **`app.py`**
   - Maneja el CRUD de ventas.
   - Expone endpoints para cargar datos dinámicos (clientes/productos).
   - Ejecuta el proceso **ETL** entre `base_envio` → `base_cargue`.
   - Expone la interfaz web (`index.html`).

2. **`api_ventas.py`**
   - Devuelve el total de ventas y unidades agrupadas por categoría.
   - Se consulta desde `app.py` y desde el frontend para las visualizaciones.

---

### Proceso ETL

El proceso **Extract – Transform – Load (ETL)** migra los datos desde la base fuente (`base_envio`) hacia la base destino (`base_cargue`).

#### Etapas:
1. **Extracción:** Se leen las tablas `clientes`, `productos` y `ventas` desde MySQL.
2. **Transformación:** (en esta versión no hay limpieza, pero puede agregarse validación).
3. **Carga:** Se sobrescriben las tablas en la base destino.

El proceso se ejecuta mediante el botón **“Generar ETL”** en la interfaz web.

---

### Frontend (HTML + JS + Bootstrap + SweetAlert2)

Características:
- Interfaz responsiva con **Bootstrap 5**.
- Alertas visuales y confirmaciones con **SweetAlert2**.
- Selects dinámicos para clientes y productos (consultan el backend).
- Tabla resumen de ventas por categoría.
- Botón “Generar ETL” que lanza el proceso con confirmación.

---

### Dashboard (Power BI)

El archivo **`visualizacion_dashboard.pbix`** contiene el dashboard conectado a la base de datos `base_cargue`.  
Incluye:
- Gráficas de ventas por categoría.
- Ventas totales y unidades vendidas.
- Filtros interactivos de fechas y productos.

Para abrirlo:
1. Instala **Power BI Desktop** (gratuito).
2. Abre el archivo `visualizacion_dashboard.pbix`.
3. Si es necesario, actualiza las credenciales de conexión (base MySQL `base_cargue`).
4. Haz clic en **Actualizar** para traer los datos más recientes.

---

## Requisitos

- Python 3.10+
- MySQL Server
- Power BI Desktop
- Librerías Python:
  ```bash
  pip install flask mysql-connector-python sqlalchemy pandas pymysql requests flask-cors


