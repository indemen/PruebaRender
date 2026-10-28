from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def inicio():
    return jsonify({
        "mensaje": "¡Hola desde Render!",
        "estado": "activo",
        "servicio": "API de prueba"
    })

@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(debug=True)
