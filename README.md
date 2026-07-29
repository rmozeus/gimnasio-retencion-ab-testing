# 📊 Análisis de Engagement de Clientes y Correlación de Gastos por Asistencia: A/B Testing y Pipeline de Datos

Este repositorio contiene un pipeline de análisis de datos *end-to-end* en Python, SQL y Matplotlib para evaluar el nivel de engagement obtenido entre dos planes de suscripción (**Plan Tradicional** vs **Plan Pro**)a un centro de entrenamiento halterofílico.

## 🛠️ Tecnologías y Librerías Utilizadas
* **Python 3**
* **SQLite3** (Motor de base de datos relacional)
* **Pandas** (Tratamiento, curado y agregación avanzada de datos)
* **SciPy (`scipy.stats`)** (Evaluación de hipótesis mediante prueba $t$ de Student)

---

## 📈 Resumen Estadístico de los Planes

| Tipo de Plan | Media | Desviación Estándar | Mediana | Rango Intercuartil (IQR) |
| :--- | :--- | :--- | :--- | :--- |
| **Plan Pro** | 15 | 1.8257 | 15 | 2.00 |
| **Plan Tradicional** | 8.4 | 1.5055 | 8.5 | 1.75 |

---

## Resultados del Testeo A/B

* **Estadístico $t$:** $-8.8196$
* **$p$-value:** $< 0.0000001$ ($0.000000$)
* **Nivel de significancia ($\alpha$):** $0.05$

### Conclusión de Negocio
Se rechaza la hipótesis nula ($H_0$). El **Plan Pro** genera un incremento estadísticamente significativo del **$78.6\%$ en el número de clientes recurrentes** ($7$ clientes). Se recomienda ampliamente migrar la oferta comercial para posicionar el Plan Pro como la suscripción principal. 
Oportunidad de Cross-Selling: La alta asistencia del Plan Pro abre un canal ideal para monetizar productos secundarios (suplementos y mercancía).