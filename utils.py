import pandas as pd
import matplotlib.pyplot as plt

## Creamos función de gráfico de valores faltantes en DF
def plot_missing(df):

    # Calculamos el porcentaje de valores faltantes por columna
    missing_percent = df.isnull().mean()*100
        
    # Filtramos las columnas con valores faltantes
    missing_percent = missing_percent[missing_percent>0].sort_values(ascending = False)

    if missing_percent.empty:
        print("No hay valores nulos en el DataFrame")
        return
    
    # Generamos la gráfica
    plt.figure(figsize=(10,6))
    missing_percent.plot(kind = 'bar', color = 'skyblue', edgecolor='black')
    plt.title('Porcentaje valores faltantes por columna', fontsize = 14)
    plt.xlabel('Columnas', fontsize = 14)
    plt.ylabel('Porcentae valores faltantes (%)', fontsize = 14)
    plt.xticks(rotation = 45, ha = 'right', fontsize = 10)
    plt.tight_layout()
    plt.show()