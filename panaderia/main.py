import pandas as pd


#Cargar los datos en pandas
df = pd.read_csv('panes.csv')

print(df)


#Limpieza de datos
# Eliminar filas con datos faltantes
df = df.dropna(subset=['pan'])

df = df.dropna(subset=['ventas'])

df = df.dropna(subset=['panaderia'])

#Indexar

ventas_mayores = df[df['ventas']>100]
print("Ventas mayores a 100")
print(ventas_mayores)

ventas_menores = df[df['ventas']<100]
print("Ventas menores a 100")
print(ventas_menores[['panaderia', 'ventas']])






