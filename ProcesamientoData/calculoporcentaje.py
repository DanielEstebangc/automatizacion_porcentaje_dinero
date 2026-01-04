

def calcular_porcentaje(total):
    if total == 0:
        return {}

    esencial = 0.40 * total
    estabilidad = 0.15 * total
    disfrute = 0.15 * total
    inversion = 0.30 * total

    return {
        "Esencial (40%)": esencial,
        "Estabilidad (15%)": estabilidad,
        "Disfrute (15%)": disfrute,
        "Inversión (30%)": inversion
    }

    return porcentajes



