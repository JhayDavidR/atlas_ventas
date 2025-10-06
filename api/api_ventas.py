from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Julian1000120395**',  # si tu usuario tiene contraseña, colócala aquí
    'database': 'base_cargue'
}

@app.route('/ventas_por_categoria', methods=['GET'])
def ventas_por_categoria():
    conn = None
    try:
        # Conexión a la base de datos
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)

        # Consulta actualizada según tus tablas reales
        query = """
        SELECT 
            p.categoria AS categoria,
            SUM(p.precio * v.cantidad) AS total_ventas,
            SUM(v.cantidad) AS total_unidades
        FROM ventas v
        INNER JOIN productos p ON v.id_producto = p.id_producto
        GROUP BY p.categoria
        ORDER BY total_ventas DESC;

                """

        cursor.execute(query)
        resultados = cursor.fetchall()

        return jsonify({
            "status": "success",
            "data": resultados
        }), 200

    except mysql.connector.Error as e:
        return jsonify({
            "status": "error",
            "message": f"Error MySQL: {str(e)}"
        }), 500

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

    finally:
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
