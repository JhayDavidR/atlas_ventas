-- ==============================
-- 1. Escribe una consulta para obtener las ventas totales por mes y categoría de producto.
-- ==============================

SELECT 
    DATE_FORMAT(v.fecha_venta, '%Y-%m') AS mes,
    p.categoria,
    SUM(v.cantidad * p.precio) AS total_ventas
FROM ventas v
INNER JOIN productos p ON v.id_producto = p.id_producto
GROUP BY DATE_FORMAT(v.fecha_venta, '%Y-%m'), p.categoria
ORDER BY mes, total_ventas DESC;

-- ==============================
-- 2. Obtén el TOP 5 de clientes con mayores compras en el último año.
-- ==============================
SELECT 
    c.id_cliente,
    c.nombre AS cliente,
    SUM(v.cantidad * p.precio) AS total_compras
FROM ventas v
INNER JOIN clientes c ON v.id_cliente = c.id_cliente
INNER JOIN productos p ON v.id_producto = p.id_producto
WHERE v.fecha_venta >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
GROUP BY c.id_cliente, c.nombre
ORDER BY total_compras DESC
LIMIT 5;

-- ==============================
-- 3. Crea una vista que muestre: cliente, ciudad, total de compras, última fecha de compra.
-- ==============================

CREATE OR REPLACE VIEW vista_clientes_compras AS
SELECT 
    c.id_cliente,
    c.nombre AS cliente,
    c.ciudad,
    SUM(v.cantidad * p.precio) AS total_compras,
    MAX(v.fecha_venta) AS ultima_compra
FROM clientes c
LEFT JOIN ventas v ON c.id_cliente = v.id_cliente
LEFT JOIN productos p ON v.id_producto = p.id_producto
GROUP BY c.id_cliente, c.nombre, c.ciudad;
