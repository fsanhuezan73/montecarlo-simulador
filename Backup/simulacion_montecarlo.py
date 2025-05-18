import numpy as np
import matplotlib.pyplot as plt

# Configurar simulaciones
NUM_SIMULACIONES = 10000

# 1. Distribución Uniforme
def simular_uniforme(min_val, max_val):
    muestras = np.random.uniform(low=min_val, high=max_val, size=NUM_SIMULACIONES)
    return muestras

# 2. Distribución Normal
def simular_normal(media, desviacion):
    muestras = np.random.normal(loc=media, scale=desviacion, size=NUM_SIMULACIONES)
    return muestras

# 3. Distribución Triangular
def simular_triangular(pesimista, probable, optimista):
    muestras = np.random.triangular(left=pesimista, mode=probable, right=optimista, size=NUM_SIMULACIONES)
    return muestras

# Función para mostrar estadísticas y gráfico
def mostrar_resultados(muestras, titulo):
    media = np.mean(muestras)
    std_dev = np.std(muestras)
    p10 = np.percentile(muestras, 10)
    p50 = np.percentile(muestras, 50)
    p90 = np.percentile(muestras, 90)

    print(f"\n--- {titulo} ---")
    print(f"Media: {media:.2f}")
    print(f"Desviación estándar: {std_dev:.2f}")
    print(f"P10: {p10:.2f}")
    print(f"P50 (mediana): {p50:.2f}")
    print(f"P90: {p90:.2f}")

    plt.hist(muestras, bins=50, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title(f'Distribución: {titulo}')
    plt.xlabel('Valor simulado')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.show()


# Ejecutar simulaciones
if __name__ == "__main__":
    # Uniforme entre 10 y 30
    datos_uniforme = simular_uniforme(10, 30)
    mostrar_resultados(datos_uniforme, "Uniforme (10, 30)")

    # Normal con media 20 y desviación estándar 5
    datos_normal = simular_normal(20, 5)
    mostrar_resultados(datos_normal, "Normal (μ=20, σ=5)")

    # Triangular con pesimista=10, probable=20, optimista=30
    datos_triangular = simular_triangular(10, 20, 30)
    mostrar_resultados(datos_triangular, "Triangular (10, 20, 30)")
