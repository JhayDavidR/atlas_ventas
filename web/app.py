from flask import Flask, render_template, request, jsonify
import requests
import mysql.connector
import pandas as pd
import configparser
from sqlalchemy import create_engine
import pymysql
from config.db_config import get_db_config

app = Flask(__name__)

DB_CONFIG = get_db_config('mysql_base_envio')


# --- Página principal ---
@app.route('/')
def index():
    return render_template('index.html')

# --- Listar clientes ---
@app.route('/clientes', methods=['GET'])
def listar_clientes():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id_cliente, nombre FROM clientes")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)

# --- Listar productos ---
@app.route('/productos', methods=['GET'])
def listar_productos():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id_producto, nombre_producto FROM productos")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)

# --- Registrar venta ---
@app.route('/agregar_venta', methods=['POST'])
def agregar_venta():
    try:
        data = request.get_json()
        cliente_id = data.get('cliente_id')
        producto_id = data.get('id_producto')
        cantidad = data.get('cantidad')
        fecha_venta = data.get('fecha_venta')

        if not all([cliente_id, producto_id, cantidad, fecha_venta]):
            return jsonify({"status": "error", "message": "Faltan datos"}), 400

        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        query = """
            INSERT INTO ventas (id_cliente, id_producto, cantidad, fecha_venta)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (cliente_id, producto_id, cantidad, fecha_venta))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"status": "success", "message": "Venta registrada correctamente"}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# --- Ver ventas (consume la API de api_ventas.py) ---
@app.route('/ventas_por_categoria', methods=['GET'])
def ver_ventas():
    response = requests.get('http://127.0.0.1:5000/ventas_por_categoria')
    data = response.json()
    return jsonify(data)

# --- Ejecutar ETL ---
@app.route('/ejecutar_etl', methods=['POST'])
def ejecutar_etl():
    try:

        SOURCE_DB = get_db_config('mysql_base_envio')
        TARGET_DB = get_db_config('mysql_base_cargue')

        TABLES = ["clientes", "productos", "ventas"]
        data_frames = {}

        source_conn = mysql.connector.connect(**SOURCE_DB)
        for table in TABLES:
            query = f"SELECT * FROM {table}"
            data_frames[table] = pd.read_sql(query, source_conn)
        source_conn.close()

        target_engine = create_engine(
            f"mysql+pymysql://{TARGET_DB['user']}:{TARGET_DB['password']}@{TARGET_DB['host']}/{TARGET_DB['database']}"
        )

        for table, df in data_frames.items():
            df.to_sql(table, con=target_engine, if_exists='replace', index=False)

        return jsonify({"status": "success", "message": "Proceso ETL completado correctamente."})

    except Exception as e:
        return jsonify({"status": "error", "message": f"Error en ETL: {str(e)}"})


if __name__ == '__main__':
    app.run(port=5001, debug=True)
