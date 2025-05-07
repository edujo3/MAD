from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return '✅ COMET Server funcionando correctamente'

@app.route('/receive_image', methods=['POST'])
def receive_image():
    try:
        image = request.files.get('image')
        if not image:
            return jsonify({'error': 'No se recibió ninguna imagen'}), 400

        print(f"📥 Imagen recibida: {image.filename} (tipo: {image.content_type})")

        # Opcionalmente puedes guardarla si quieres en el servidor
        # image.save(f"/tmp/{image.filename}")

        return jsonify({'message': 'Imagen recibida correctamente'}), 200

    except Exception as e:
        print(f"❌ Error al procesar imagen: {str(e)}")
        return jsonify({'error': 'Error procesando la imagen'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
