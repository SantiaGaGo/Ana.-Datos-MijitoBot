#TIENEN SMARTPHONE LOS ADULTOS MAYORES EN BOGOTA?
import pandas as pd
import matplotlib.pyplot as plt
# Configurar pandas para mostrar más columnas en la consola
pd.set_option('display.max_columns', None)

# Cargar el archivo Excel en un DataFrame
df = pd.read_excel(r'C:\Users\santi\Downloads\datos DANE\Datos Para Analisis Capitulo I (DANE).xlsx', sheet_name='TICS')
df2 = pd.read_excel(r'C:\Users\santi\Downloads\datos DANE\Datos Para Analisis Capitulo E (DANE).xlsx', sheet_name='EDAD')

# Filtrar el DataFrame 1 (df) basado en la condición del DataFrame 2 (df2)
df_filtrado = df[df['DIRECTORIO_PER'].isin(df2.loc[df2['NPCEP4'] >= 60, 'DIRECTORIO_PER'])]

# Filtrar el DataFrame filtrado (df_filtrado) para incluir solo las filas con valor "1" en la columna NPCIP12 (PERSONAS QUE SI TIENEN CEL)
df_filtrado_1 = df_filtrado[df_filtrado['NPCIP12'] == 1]

# Calcular las proporciones de valores "1" y "2" en la columna NPCIP12A del DataFrame filtrado con valor "1" en NPCIP12
proporciones_npcip12a = df_filtrado_1['NPCIP12A'].value_counts(normalize=True) * 100

# Calcular las proporciones de valores "1" y "2" en la columna NPCIP12B del DataFrame filtrado con valor "1" en NPCIP12
proporciones_npcip12b = df_filtrado_1['NPCIP12B'].value_counts(normalize=True) * 100

# Imprimir las proporciones de NPCIP12A y NPCIP12B
print("Proporciones de NPCIP12A:")
print(proporciones_npcip12a)
print("\nProporciones de NPCIP12B:")
print(proporciones_npcip12b)

# Crear gráficos de barras mejorados con etiquetas de datos
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Gráfico para NPCIP12A
axs[0].bar(range(len(proporciones_npcip12a)), proporciones_npcip12a.values, color=['green', 'blue'], alpha=0.7)
axs[0].set_title('Proporciones de NPCIP12A')
axs[0].set_xticks(range(len(proporciones_npcip12a)))  # Añadir marcas en el eje x
axs[0].set_xticklabels(proporciones_npcip12a.index)  # Etiquetas en el eje x
axs[0].set_ylabel('Proporción (%)')

# Agregar etiquetas de datos con los porcentajes
for i, valor in enumerate(proporciones_npcip12a.values):
    axs[0].text(i, valor + 1, f'{valor:.2f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Gráfico para NPCIP12B
axs[1].bar(range(len(proporciones_npcip12b)), proporciones_npcip12b.values, color=['green', 'blue'], alpha=0.7)
axs[1].set_title('Proporciones de NPCIP12B')
axs[1].set_xticks(range(len(proporciones_npcip12b)))  # Añadir marcas en el eje x
axs[1].set_xticklabels(proporciones_npcip12b.index)  # Etiquetas en el eje x
axs[1].set_ylabel('Proporción (%)')

# Agregar etiquetas de datos con los porcentajes
for i, valor in enumerate(proporciones_npcip12b.values):
    axs[1].text(i, valor + 1, f'{valor:.2f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()