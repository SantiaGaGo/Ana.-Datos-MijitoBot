#Analisis Proporciones de los dispositivos mas usados en los hogares Bogotanos para acceder a Internet

import pandas as pd
import matplotlib.pyplot as plt
# Configurar pandas para mostrar más filas y columnas en la consola

pd.set_option('display.max_columns', None) 
# Cargar el archivo Excel en un DataFrame
df = pd.read_excel(r'C:\Users\santi\Downloads\datos DANE\Datos Para Analisis Capitulo I (DANE).xlsx', sheet_name='TICS')
df2 = pd.read_excel(r'C:\Users\santi\Downloads\datos DANE\Datos Para Analisis Capitulo E (DANE).xlsx', sheet_name='EDAD')

# Filtrar el DataFrame 1 (df) basado en la condición del DataFrame 2 (df2)
df_filtrado = df[df['DIRECTORIO_PER'].isin(df2.loc[df2['NPCEP4'] >= 60, 'DIRECTORIO_PER'])]

# Seleccionar las columnas relevantes que representan las preguntas y las respuestas
columnas_preguntas = ['NPCIP6A', 'NPCIP6B', 'NPCIP6C', 'NPCIP6D', 'NPCIP6E', 'NPCIP6F', 'NPCIP6G', 'NPCIP6H']

#Variables totales: 8
# Computador de escritorio ------> ID = "V5150", NOMBRE = "NPCIP6A", TIPO = discrete, FORMATO = numeric
# Computador Portatil -----------> ID = "V5151", NOMBRE = "NPCIP6B", TIPO = discrete, FORMATO = numeric
# Tablet ------------------------> ID = "V5152", NOMBRE = "NPCIP6C", TIPO = discrete, FORMATO = numeric
# Telefono ----------------------> ID = "V5153", NOMBRE = "NPCIP6D", TIPO = discrete, FORMATO = numeric
# Consolas de videojuegos -------> ID = "V5154", NOMBRE = "NPCIP6E", TIPO = discrete, FORMATO = numeric
# Smart TV televisor inte. ------> ID = "V5155", NOMBRE = "NPCIP6F", TIPO = discrete, FORMATO = numeric
# Reproductores de musica  ------> ID = "V5156", NOMBRE = "NPCIP6G", TIPO = discrete, FORMATO = numeric
# Otro --------------------------> ID = "V5157", NOMBRE = "NPCIP6H", TIPO = discrete, FORMATO = numeric
#Disponible en documentacion https://microdatos.dane.gov.co/index.php/catalog/743/data-dictionary


# Calcular la proporción de cada valor para cada pregunta
# Este método cuenta la frecuencia de cada valor único en la columna y normaliza los resultados para obtener las proporciones. 
# Luego, se multiplica por 100 para expresar las proporciones en porcentaje. Los valores son "1" = SI y "2" = NO
proporciones_por_pregunta = {}
for columna in columnas_preguntas:
    proporciones_valores = df_filtrado[columna].value_counts(normalize=True) * 100
    proporciones_por_pregunta[columna] = proporciones_valores

# Crear el gráfico de barras
df_proporciones = pd.DataFrame(proporciones_por_pregunta).T
colors = ['#1f77b4', '#ff7f0e']  # Colores para "Sí" y "No"
ax = df_proporciones.plot(kind='bar', stacked=True, color=colors)

# Mostrar etiquetas de datos en las barras
for p in ax.patches:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy()
    ax.annotate(f'{height:.4f}%', (x + width / 2, y + height * 0.5), ha='center', va='center', fontsize=10, fontweight='bold')

# Cambiar nombres de las columnas en el gráfico
nuevas_etiquetas = ['PC Escritorio', 'PC Portatil', 'Tablet', 'Telefono', 'Consolas', 'Smart TV', 'Reproductores', 'Otro']
plt.xticks(range(len(nuevas_etiquetas)), nuevas_etiquetas, rotation=45, ha='right')


plt.xlabel('Pregunta')
plt.ylabel('Proporción (%)')
plt.title('Proporción de Respuestas "Sí" y "No" por Pregunta')
plt.legend(title='Valor', labels=['Sí', 'No'])

plt.tight_layout()
plt.show()