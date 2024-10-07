from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('urban_farming.db')
    conn.row_factory = sqlite3.Row
    return conn

# Endpoint para receber e salvar os dados no banco de dados
@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()

    # Coletar todos os dados do JSON recebido
    sensor_id = data.get('sensor_id', 1)  # Valor padrão de sensor_id se não estiver presente
    temperature = data.get('temperatura')
    humidity = data.get('umidade')
    distancia_ultrassom = data.get('distancia_ultrassom', None)  # Valor padrão None
    luminosidade_leds = data.get('luminosidade_leds', None)  # Valor padrão None
    status_bomba_agua = data.get('status_bomba_agua', 'desconhecido')  # Valor padrão se não for enviado
    status_ventoinha = data.get('status_ventoinha', 'desconhecido')  # Valor padrão se não for enviado
    
    # Pegar o horário atual para armazenar na coluna data_hora
    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Conectar ao banco e salvar os dados na tabela 'dados_coletados'
    conn = get_db_connection()
    conn.execute(
        '''INSERT INTO dados_coletados (sensor_id, data_hora, temperatura, umidade, distancia_ultrassom, 
                                        luminosidade_leds, status_bomba_agua, status_ventoinha)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
        (sensor_id, data_hora, temperature, humidity, distancia_ultrassom, luminosidade_leds, 
         status_bomba_agua, status_ventoinha)
    )
    conn.commit()
    conn.close()

    return jsonify({"status": "success", "data": data}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)