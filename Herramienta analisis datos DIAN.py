# **********************************************************************
# *                                                                    *
# *                       LICENCIA DE USO                              *
# *                                                                    *
# **********************************************************************
#
# Este programa es de código abierto y se proporciona tal cual, sin garantías de ningún tipo.
# Puedes utilizar, modificar y distribuir este programa libremente, siempre y cuando respetes las siguientes condiciones:
# 1. Incluye este aviso de licencia en todas las copias o modificaciones que realices.
# 2. No me responsabilizo de ningún daño o problema derivado del mal uso o modificaciones de este programa.
#
# ------------------------ Consejos del Adviser -----------------------
# 1. Si modificas este programa, asegúrate de comprender su funcionamiento.
# 2. Siempre respeta los derechos de autor y las licencias de las bibliotecas utilizadas.
# 3. Cualquier duda contacta al creador directamente egamboag@unal.edu.co
# **********************************************************************

import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo Excel en un DataFrame
df = pd.read_excel(r'C:\Users\santi\Downloads\datos DANE\Datos Para Analisis Capitulo I (DANE).xlsx', sheet_name='TICS')

# Seleccionar las columnas relevantes que representan las preguntas y las respuestas
columnas_preguntas = ['NPCIP6A', 'NPCIP6B', 'NPCIP6C', 'NPCIP6D', 'NPCIP6E', 'NPCIP6F', 'NPCIP6G', 'NPCIP6H']

# Calcular la proporción de cada valor para cada pregunta
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