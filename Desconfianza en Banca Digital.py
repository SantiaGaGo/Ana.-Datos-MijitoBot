#¿Cuál es la razón principal para
# no usar el internet en compras ni
# en servicios de banca
# electrónica? PARA LOS ADULTOS MAYORES

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los archivos de Excel en dos DataFrame
df = pd.read_excel(r'C:\Users\santi\Downloads\datos DANE\Datos Para Analisis Capitulo I (DANE).xlsx', sheet_name='TICS')
df2 = pd.read_excel(r'C:\Users\santi\Downloads\datos DANE\Datos Para Analisis Capitulo E (DANE).xlsx', sheet_name='EDAD')
# Seleccionar las columnas relevantes que representan las preguntas y las respuestas
#La Pregunta literal es: ""
columna_respuestas = 'NPCIP8DE'
#Variables totales: 1 (ID = 5177)
#Disponible  en documentacion https://microdatos.dane.gov.co/index.php/catalog/743/data-dictionary

# Este método cuenta la frecuencia de cada valor único en la columna y normaliza los resultados para obtener las proporciones. 
# Luego, se multiplica por 100 para expresar las proporciones en porcentaje.
# Los valores son:
# 1. Falta de seguridad 
# 2. No sabe cómo
# 3. No tiene cuentas bancarias, ni tarjetas débito o crédito 
#4. Otra razón

# Filtrar el DataFrame 1 (df) basado en la condición del DataFrame 2 (df2) (SOLO MAYORES DE 60 AÑOS)
df_filtrado = df[df['DIRECTORIO_PER'].isin(df2.loc[df2['NPCEP4'] >= 60, 'DIRECTORIO_PER'])]

# Calcular el porcentaje de cada valor en la columna filtrada con respecto al total de datos
porcentaje_valores = df_filtrado[columna_respuestas].value_counts(normalize=True) * 100

# Crear la gráfica de pastel
plt.figure(figsize=(8, 8))  # Tamaño de la gráfica
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']  # Colores para las porciones
plt.pie(porcentaje_valores, labels=porcentaje_valores.index, autopct='%1.1f%%', startangle=140, colors=colors, wedgeprops={'edgecolor': 'black'})

# Agregar etiquetas de datos en cada porción
for i, (label, porcentaje) in enumerate(zip(porcentaje_valores.index, porcentaje_valores)):
    plt.text(0.5, 0.5, f'{label}: {porcentaje:.2f}%', fontsize=10, ha='center', va='center', color='white')

plt.title('¿Cuál es la razón principal para no usar el internet en compras ni en servicios de banca electrónica?', fontsize=14)
plt.axis('equal')  # Mantener aspecto de círculo
plt.legend(title='Respuestas', labels=porcentaje_valores.index, loc='upper right')
plt.tight_layout()
plt.show()
# Calcular el porcentaje de cada valor en la columna con respecto al total de datos

print("DataFrame utilizado después del filtro:")
print(df_filtrado)
#49997 encuestados Aprox.