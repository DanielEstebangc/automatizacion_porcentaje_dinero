import pandas as pd
import os

def guardar_datos(ruta_completa, datos):
    # Si el archivo existe, lo abrimos y combinamos
    if os.path.exists(ruta_completa):
        existente = pd.read_excel(ruta_completa)
        datos_final = pd.concat([existente, datos], ignore_index=True)
    else:
        datos_final = datos  # Si no existe, simplemente lo usamos

    # Guardamos (sobrescribiendo, pero ya con los nuevos datos incluidos)
    datos_final.to_excel(ruta_completa, index=False)

    print("✅ Datos guardados correctamente en:", ruta_completa)