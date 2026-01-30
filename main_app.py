import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración estética
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

def run_eda(file_path):
    # 1. Carga de datos
    df = pd.read_csv(file_path)
    df['Fecha_Ultima_Auditoria'] = pd.to_datetime(df['Fecha_Ultima_Auditoria'])
    
    print("--- Información General ---")
    print(df.info())
    print("\n--- Primeras Filas ---")
    print(df.head())

    # 2. Análisis Descriptivo
    print("\n--- Estadísticas Descriptivas ---")
    print(df.describe())

    # 3. Visualizaciones
    
    # A. Distribución de Producción por Departamento
    plt.figure()
    sns.boxplot(data=df, x='Departamento', y='Produccion_Anual_Ton', palette='viridis')
    plt.title('Distribución de Producción Anual por Departamento')
    plt.xticks(rotation=45)
    plt.show()

    # B. Relación entre Área y Producción (¿Es lineal?)
    plt.figure()
    sns.scatterplot(data=df, x='Area_Hectareas', y='Produccion_Anual_Ton', hue='Nivel_Tecnificacion')
    plt.title('Área vs Producción (Color por Nivel de Tecnificación)')
    plt.show()

    # C. Conteo de Cultivos
    plt.figure()
    sns.countplot(data=df, y='Tipo_Cultivo', order=df['Tipo_Cultivo'].value_counts().index, palette='magma')
    plt.title('Frecuencia de Tipos de Cultivo')
    plt.show()

    # 4. Análisis de Valor Económico
    # Calculamos el valor estimado de la producción por finca
    df['Valor_Total_Estimado'] = df['Produccion_Anual_Ton'] * df['Precio_Venta_Por_Ton_COP']
    
    print("\n--- Top 5 Departamentos por Valor de Producción Estimado ---")
    top_depto = df.groupby('Departamento')['Valor_Total_Estimado'].sum().sort_values(ascending=False)
    print(top_depto.head())

    # 5. Impacto de la Tecnificación
    plt.figure()
    sns.barplot(data=df, x='Nivel_Tecnificacion', y='Produccion_Anual_Ton', 
                hue='Sistema_Riego_Tecnificado', estimator='mean')
    plt.title('Producción Promedio según Tecnificación y Riego')
    plt.show()

# Ejecutar el análisis
if __name__ == "__main__":
    run_eda('agro_colombia.csv')
