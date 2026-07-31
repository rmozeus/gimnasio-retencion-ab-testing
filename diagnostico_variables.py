import pandas as pd
import statsmodels.api as sm

# 1. Cargar datos
df = pd.read_csv('gimnasio_multivariable.csv')

X = df[['asistencias_mes']]
y = df['gasto_suplementos']

# NOTA TÉCNICA: statsmodels requiere agregar manualmente la columna de unos para el Intercepto (b0)
X_con_constante = sm.add_constant(X)

# 2. Ajustar el modelo OLS
modelo_stats = sm.OLS(y, X_con_constante).fit()

# 3. Imprimir el Reporte Médico Completo del Modelo
print(modelo_stats.summary())