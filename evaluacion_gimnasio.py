import sqlite3
import pandas as pd
import scipy.stats as stats

# Leer y curar los datos de las tablas

df_raw = pd.read_csv('gimnasio_retencion.csv')

conexion = sqlite3.connect('gimnasio.db')

df_raw.to_sql('usuarios', conexion, if_exists='replace', index=False)

query = """
SELECT
    id_usuario,
    tipo_plan,
    asistencias_mes,
    gasto_suplementos,
    CASE
        WHEN asistencias_mes >= 12 THEN 'Sí'
        ELSE 'No'
    END AS usuario_frecuente
FROM usuarios;
"""

df_gimnasio = pd.read_sql_query(query, conexion)
conexion.close()

# Proceso analítico con Pandas

df_resumen_plan = df_gimnasio.groupby('tipo_plan')['asistencias_mes'].agg(
    Media='mean',
    Desviacion='std',
    Mediana='median',
    Conteo='count',
    IQR=lambda x: x.quantile(0.75) - x.quantile(0.25)
)

print("\n--- RESUMEN PLAN PRO DEL GIMNASIO ---")
print(df_resumen_plan)

asistencias_tradicional = df_gimnasio[df_gimnasio['tipo_plan'] == 'Tradicional']['asistencias_mes']
asistencias_pro = df_gimnasio[df_gimnasio['tipo_plan'] == 'Plan_Pro']['asistencias_mes']

estat_t, p_valor = stats.ttest_ind(asistencias_tradicional, asistencias_pro)

print("--- TESTEO DE HIPÓTESIS A/B ---")
print(f"Estadístico: {estat_t:.4f}")
print(f"p-value:     {p_valor:.6f}")

if p_valor < 0.05:
    print("\n✅ CONCLUSIÓN: La Promoción B incrementa la retención con significancia estadística.")
else:
    print("\n❌ CONCLUSIÓN: No hay suficiente evidencia estadística para comprobar una mayor retención.")

# Resumen multivariable para analizar otros beneficios
resumen_multivariable = df_gimnasio.groupby('tipo_plan').agg(
    asistencias_promedio=('asistencias_mes', 'mean'),
    gasto_suplementos_promed=('gasto_suplementos', 'mean'),
    gasto_suplementos_mediana=('gasto_suplementos', 'median')
)

# Correlación asistencia con nivel de gasto en suplementos
correlacion = df_gimnasio['asistencias_mes'].corr(df_gimnasio['gasto_suplementos'])

print("\n--- Resumen Multivariable ---")
print(resumen_multivariable)
print(f"\nCorrelación entre asistencia y gasto: {correlacion:.2f}")