import os
from flask import Flask, render_template , request, jsonify
from ProcesamientoData.calculoporcentaje import calcular_porcentaje
from ProcesamientoData.converciondata import convercion_data
from Guardadodedatos.guardardatos import guardar_datos

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("resultados.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    data = request.get_json()
    saldo = data.get("saldo")

    # 1️⃣ usar tu lógica
    porcentajes = calcular_porcentaje(saldo)

    # 2️⃣ convertir a DataFrame (como ya hacías)
    df = convercion_data(porcentajes, saldo)

    # 3️⃣ convertir DataFrame a algo que JS entienda
    resultado = df.to_dict(orient="records")

    #  # 🔹 construir ruta
    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # ruta_archivo = os.path.join(
    #     BASE_DIR,
    #     "Datos",
    #     "historial.xlsx"
    # )

    # guardar_datos(ruta_archivo, df)

    return jsonify(resultado)

# # Ejecutar la aplicación en test

# if __name__ == "__main__":
#     app.run(debug=True)

# Ejecutar la aplicación en producción

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render pasa el puerto por env
    app.run(host="0.0.0.0", port=port)
