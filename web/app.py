from flask import Flask, render_template, request, jsonify
import requests
import pyodbc

app = Flask(__name__)

# Conexión a SQL Server
def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;DATABASE=base_envio;UID=root;PWD=Julian1000120395**;'
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar_venta', methods=['POST'])
def agregar_venta():
    cliente_id = request.form['cliente_id']
    producto_id = request.form['producto_id']
    cantidad = request.form['cantidad']

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ventas (id_cliente, id_producto, cantidad, fecha_venta) VALUES (?, ?, ?, GETDATE())",
                   (cliente_id, producto_id, cantidad))
    conn.commit()
    conn.close()

    return jsonify({'mensaje': 'Venta registrada correctamente'})

@app.route('/ver_ventas')
def ver_ventas():
    # Consumir la API que ya creaste
    response = requests.get('http://127.0.0.1:5001/ventas_por_categoria')
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
