# Inicializa la sesión de Spark
spark = SparkSession.builder.appName('Tarea3').getOrCreate()

# Define la ruta del archivo .csv en HDFS
file_path = 'hdfs://localhost:9000/Tarea3/query.csv'

# Lee el archivo .csv
df = spark.read.format('csv').option('header', 'true').option('inferSchema', 'true').load(file_path)

# 1. Transformación para ajustar nombres, formato de fecha (DD/MM/YYYY) y tipo de dato
df_resultado = df.select(
    F.col("valor").cast("double").alias("VALOR"),
    F.upper(F.col("unidad")).alias("UNIDAD"),
    F.date_format(F.col("vigenciadesde"), "dd/MM/yyyy").alias("VIGENCIADESDE"),
    F.date_format(F.col("vigenciahasta"), "dd/MM/yyyy").alias("VIGENCIAHASTA")
).orderBy(F.col("vigenciadesde").desc())

# 2. Imprimir esquema formateado
df_resultado.printSchema()

# 3. Mostrar la tabla con formato idéntico al requerimiento
df_resultado.show(20, truncate=False)

# --- Consultas adicionales de tu tarea ---

# Estadísticas básicas
df_resultado.summary().show()

# Filtrar por valor mayor a 5000
print("Días con valor mayor a 5000\n")
dias = df_resultado.filter(F.col('VALOR') > 5000)
dias.show()

# Ordenar de mayor a menor por VALOR
print("Valores ordenados de mayor a menor\n")
sorted_df = df_resultado.sort(F.col("VALOR").desc())
sorted_df.show()

input("--- SPARK UI ACTIVA --- Presiona ENTER cuando termines de revisar la página web...")

