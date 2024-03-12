from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    message = data['Body']

    # Procesar el mensaje y generar el documento personalizado
    nombre = message  # Supongamos que el mensaje es solo el nombre del usuario

    with open('plantilla.txt', 'r') as file:
        plantilla = file.read()

    documento_personalizado = plantilla.replace('{{nombre}}', nombre)

    # Aquí puedes guardar el documento en el servidor o enviarlo por mensaje a través de WhatsApp

    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True)
