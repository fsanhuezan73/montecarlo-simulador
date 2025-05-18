import numpy as np

def calcular_estadisticas(muestras: np.ndarray) -> dict:
    """
    Dadas unas muestras simuladas devuelve:
      - media
      - desviación estándar
      - percentiles 10, 50, 90
    """
    return {
        "media": round(np.mean(muestras), 2),
        "desviacion_estandar": round(np.std(muestras), 2),
        "p10": round(np.percentile(muestras, 10), 2),
        "p50": round(np.percentile(muestras, 50), 2),
        "p90": round(np.percentile(muestras, 90), 2),
    }