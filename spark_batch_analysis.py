from pyspark.sql import SparkSession

# 1. Inicializar la sesión de Spark de manera eficiente
spark = SparkSession.builder \
    .appName("AnalisisColombianosUNAD") \
    .master("local[*]") \
    .getOrCreate()

# 2. Cargar el archivo CSV optimizando la lectura y el esquema
archivo = "datos.csv"

df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("encoding", "UTF-8") \
    .csv(archivo)

print("--- ¡DATOS CARGADOS EXITOSAMENTE CON SPARK! ---")
# Mostrar las primeras 5 filas sin truncar los textos largos
df.show(5, truncate=False)

# 3. Mostrar el conteo total de registros procesados
print("--- TOTAL DE REGISTROS EN EL DATASET ---")
print(f"Filas totales: {df.count()}")

# Detener la sesión de Spark correctamente
spark.stop()
