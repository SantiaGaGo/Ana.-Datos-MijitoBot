#Analisis Proporciones de Para que se usa internet en los hogares Bogotanos 
# Se excluye la búsqueda de información con fines de educación y aprendizaje

import pandas as pd
import matplotlib.pyplot as plt
# Configurar pandas para mostrar más columnas en la consola

pd.set_option('display.max_columns', None) 
# Cargar el archivo Excel en un DataFrame
df = pd.read_excel(r'C:\Users\santi\Downloads\datos DANE\Datos Para Analisis Capitulo I (DANE).xlsx', sheet_name='TICS')
df2 = pd.read_excel(r'C:\Users\santi\Downloads\datos DANE\Datos Para Analisis Capitulo E (DANE).xlsx', sheet_name='EDAD')

# Seleccionar las columnas relevantes que representan las preguntas y las respuestas
columnas_preguntas = ['NPCIP8A', 'NPCIP8B', 'NPCIP8C', 'NPCIP8D', 'NPCIP8E', 'NPCIP8F', 'NPCIP8G', 'NPCIP8H', 'NPCIP8I', 'NPCIP8K', 'NPCIP8J']

#Variables totales: 11 (ID's V5166- V5176)
#Disponibles  en documentacion https://microdatos.dane.gov.co/index.php/catalog/743/data-dictionary

# Filtrar el DataFrame 1 (df) basado en la condición del DataFrame 2 (df2)
df_filtrado = df[df['DIRECTORIO_PER'].isin(df2.loc[df2['NPCEP4'] >= 60, 'DIRECTORIO_PER'])]

# Mostrar qué DataFrame se está utilizando después del filtro
print("DataFrame utilizado después del filtro:")
print(df_filtrado)

# Este método cuenta la frecuencia de cada valor único en la columna y normaliza los resultados para obtener las proporciones. 
# Luego, se multiplica por 100 para expresar las proporciones en porcentaje. Los valores son "1" = SI y "2" = NO
# Calcular la proporción de cada valor para cada pregunta en el DataFrame filtrado
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
nuevas_etiquetas = ['Información', 'Correo', 'Redes Sociales', 'Compras', 'Banca Digital', 'Aprendizaje', 'Reclamos', 'Entretenimiento', ' Medios Comunicacion', 'Trabajo', 'Otros']
plt.xticks(range(len(nuevas_etiquetas)), nuevas_etiquetas, rotation=45, ha='right')
plt.xlabel('Pregunta')
plt.ylabel('Proporción (%)')
plt.title('Para que se usa internet en los hogares Bogotanos')
plt.legend(title='Valor', labels=['Sí', 'No'])

plt.tight_layout()
plt.show()