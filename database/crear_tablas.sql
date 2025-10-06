-- base de datos
CREATE DATABASE IF NOT EXISTS base_envio;
CREATE DATABASE IF NOT EXISTS base_cargue;
USE base_envio;

-- ==============================
-- Tabla: clientes
-- ==============================
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    ciudad VARCHAR(100),
    fecha_registro DATE
);

-- ==============================
-- Tabla: productos
-- ==============================
CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre_producto VARCHAR(100),
    categoria VARCHAR(100),
    precio DECIMAL(10,2)
);
-- ==============================
-- Tabla: ventas
-- ==============================
CREATE TABLE ventas (
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_producto INT,
    fecha_venta DATE,
    cantidad INT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

