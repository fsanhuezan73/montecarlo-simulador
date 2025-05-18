import os
from flask import Flask, request, jsonify
import numpy as np
from simulation import calcular_estadisticas

app = Flask(
    __name__,
    static_folder='static',      # carpeta de tu index.html
    static_url_path=''           # sirve / → static/index.html
)

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

@app.route('/simular', methods=['POST'])
def simular():
    data = request.get_json()
    tipo = data.get("tipo")
    simulaciones = int(data.get("simulaciones", 10000))

    try:
        if tipo == "uniforme":
            minimo = float(data["min"])
            maximo = float(data["max"])
            muestras = np.random.uniform(minimo, maximo, simulaciones)

        elif tipo == "normal":
            media = float(data["media"])
            desviacion = float(data["desviacion"])
            muestras = np.random.normal(media, desviacion, simulaciones)

        elif tipo == "triangular":
            p = float(data["pesimista"])
            m = float(data["probable"])
            o = float(data["optimista"])
            # valida: optimista < probable < pesimista
            if not (o < m < p):
                return jsonify({"error":"Debe cumplirse: optimista < probable < pesimista"}), 400
            # NumPy pide (left, mode, right)
            muestras = np.random.triangular(o, m, p, simulaciones)

        else:
            return jsonify({"error":"Tipo de distribución no soportado"}), 400

        resultado = calcular_estadisticas(muestras)
        resultado["muestras"] = muestras.tolist()
        return jsonify(resultado)

    except Exception as e:
        return jsonify({"error":f"Error al procesar la simulación: {e}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=False)