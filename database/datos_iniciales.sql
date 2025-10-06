-- ==============================
-- Insertar datos: clientes
-- ==============================
INSERT INTO clientes (nombre, ciudad, fecha_registro) VALUES
('Juan Pérez', 'Bogotá', '2023-01-15'),
('María López', 'Medellín', '2023-02-20'),
('Carlos Gómez', 'Cali', '2023-03-05'),
('Ana Torres', 'Bogotá', '2023-03-25'),
('Luis Ramírez', 'Barranquilla', '2023-04-10');

-- ==============================
-- Insertar datos: productos
-- ==============================
INSERT INTO productos (categoria, precio) VALUES
('Electrónica', 500.00),
('Electrónica', 1500.00),
('Hogar', 200.00),
('Hogar', 750.00),
('Ropa', 100.00);

-- ==============================
-- Insertar datos: ventas
-- ==============================
INSERT INTO ventas (id_cliente, id_producto, fecha_venta, cantidad) VALUES
(1, 1, '2023-05-01', 2),  -- Juan Pérez - Electrónica
(1, 2, '2023-05-15', 1),  -- Juan Pérez - Electrónica
(2, 3, '2023-05-06', 3),  -- María López - Hogar
(3, 4, '2023-05-26', 1),  -- Carlos Gómez - Hogar
(4, 5, '2023-07-10', 4),  -- Ana Torres - Ropa
(5, 1, '2023-07-15', 2);  -- Luis Ramírez - Electrónica
