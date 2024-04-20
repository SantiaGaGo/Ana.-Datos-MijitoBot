#Analisis Proporciones de los dispositivos mas usados en los hogares Bogotanos para acceder a Internet

import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo Excel en un DataFrame
df = pd.read_excel(r'C:\Users\santi\Downloads\datos DANE\Datos Para Analisis Capitulo I (DANE).xlsx', sheet_name='TICS')

# Seleccionar las columnas relevantes que representan las preguntas y las respuestas
columnas_preguntas = ['NPCIP6A', 'NPCIP6B', 'NPCIP6C', 'NPCIP6D', 'NPCIP6E', 'NPCIP6F', 'NPCIP6G', 'NPCIP6H']

#Variables totales: 8
# Computador de escritorio ------> ID = "V5150", NOMBRE = "NPCIP6A", TIPO = discrete, FORMATO = numeric

# Calcular la proporción de cada valor para cada pregunta
# Este método cuenta la frecuencia de cada valor único en la columna y normaliza los resultados para obtener las proporciones. 
# Luego, se multiplica por 100 para expresar las proporciones en porcentaje. Los valores son "1" = SI y "2" = NO
proporciones_por_pregunta = {}
for columna in columnas_preguntas:
    proporciones_valores = df[columna].value_counts(normalize=True) * 100
    proporciones_por_pregunta[columna] = proporciones_valores

# Crear el gráfico de barras
df_proporciones = pd.DataFrame(proporciones_por_pregunta).T
df_proporciones.plot(kind='bar', stacked=True)
plt.xlabel('Dispositivo')
plt.ylabel('Proporción (%)')
plt.title('Dispositivos usados para acceder a internet')
plt.legend(title='Value', labels=['Si', 'No'])
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()