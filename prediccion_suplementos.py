import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# -------------------------------------------------------------------
# 1. PREPARACIÓN DE DATOS (Features X y Target y)
# -------------------------------------------------------------------
# Cargamos los datos del gimnasio
df = pd.read_csv('gimnasio_retencion.csv')

# NOTA IMPORTANTE DE SCIKIT-LEARN:
# La variable X (features) SIEMPRE debe ser una matriz 2D (DataFrame o arreglo 2D)
# La variable y (target) es un vector 1D (Serie)
X = df[['asistencias_mes']]  # Doble corchete mantiene la estructura de DataFrame (2D)
y = df['gasto_suplementos']   # Un corchete es una Serie (1D)

# -------------------------------------------------------------------
# 2. ENTRENAR EL MODELO (Ajustar la recta)
# -------------------------------------------------------------------
modelo = LinearRegression()
modelo.fit(X, y) # Aquí la computadora aprende los valores de b0 y b1

# -------------------------------------------------------------------
# 3. EXTRAER LOS PARÁMETROS APRENDIDOS POR LA IA
# -------------------------------------------------------------------
beta_0 = modelo.intercept_
beta_1 = modelo.coef_[0]

print("--- MODELO DE REGRESIÓN LINEAL ENTRENADO ---")
print(f"Intercepto (Beta 0): ${beta_0:.2f}")
print(f"Coeficiente (Beta 1): ${beta_1:.2f} por cada asistencia extra")
print(f"\nEcuación del Modelo: Gasto = {beta_0:.2f} + ({beta_1:.2f} * Asistencias)")

# -------------------------------------------------------------------
# 4. EVALUAR LA CALIDAD DEL MODELO
# -------------------------------------------------------------------
y_pred = modelo.predict(X)
r2 = r2_score(y, y_pred)

print(f"\nCoeficiente de Determinación (R²): {r2:.4f}")
print(f"Explicación: El modelo explica el {r2 * 100:.1f}% de la variabilidad del gasto.")