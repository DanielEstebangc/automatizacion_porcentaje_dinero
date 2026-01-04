import pandas as pd
import datetime as dt
from ProcesamientoData.formato_cop import formato_cop

def convercion_data(datos, saldo_total):
    fecha = dt.datetime.now()
    formateada = fecha.strftime("%d/%m/%Y")

    # 🔹 Formatear TODOS los valores de porcentaje a string
    datos_formateados = {k: formato_cop(v) for k, v in datos.items()}

    # 🔹 Crear DataFrame con STRINGS
    df = pd.DataFrame([datos_formateados])

    # 🔹 Formatear saldo total también como string
    df["Saldo Total"] = formato_cop(saldo_total)

    # 🔹 Insertar la fecha al inicio
    df.insert(0, "Fecha", formateada)

    return df
