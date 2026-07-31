import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

# 1. Cargar Datos
df = pd.read_csv('gimnasio_multivariable.csv')

# 2. Definir Features (X) y Target (y)
# Pistas de Pandas: pasamos una lista con 2 columnas para crear la matriz X (2D)
X = df[['asistencias_mes', 'horas_semana']] 
y = df['gasto_suplementos']

# 3. División Train / Test (80% entrenamiento, 20% prueba)
# random_state=42 asegura que el corte sea reproducible cada vez que corras el script
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# 4. Entrenar el modelo SOLO con el conjunto de Entrenamiento (Train)
modelo_múltiple = LinearRegression()
modelo_múltiple.fit(X_train, y_train)

# 5. Parámetros Aprendidos por la IA
intercepto = modelo_múltiple.intercept_
coef_asistencias = modelo_múltiple.coef_[0]
coef_horas = modelo_múltiple.coef_[1]

print("--- MODELO DE REGRESIÓN MULTIVARIABLE ENTRENADO ---")
print(f"Intercepto (Beta 0):         ${intercepto:.2f}")
print(f"Coef. Asistencias (Beta 1):  ${coef_asistencias:.2f} por cada asistencia extra")
print(f"Coef. Horas/Semana (Beta 2): ${coef_horas:.2f} por cada hora extra semanal")

# 6. Evaluación con Datos Invisibles (Test Set)
y_pred_test = modelo_múltiple.predict(X_test)

r2_test = r2_score(y_test, y_pred_test)
rmse_test = np.sqrt(mean_squared_error(y_test, y_pred_test))

print("\n--- EVALUACIÓN EN EL CONJUNTO DE PRUEBA (TEST SET) ---")
print(f"R² en Test:  {r2_test:.4f}")
print(f"RMSE (Error promedio de predicción): ${rmse_test:.2f} pesos")