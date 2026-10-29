# Tarea 3 - Procesamiento de Datos con Apache Spark (Batch)

## 📌 Descripción de la Solución
Este repositorio contiene la solución en **Python (PySpark)** para el procesamiento batch del dataset *"Colombianos inscritos en el Registro Ciudadano en Línea"*. El script se encarga de realizar la carga masiva del archivo CSV, la inferencia de esquemas y el procesamiento distribuido para la extracción de métricas clave, alcanzando un total procesado de **639,041 registros**.

## 🛠️ Requisitos del Entorno
* **Sistema Operativo:** Ubuntu (Máquina Virtual del curso Big Data).
* **Motor de Procesamiento:** Apache Spark 3.5.8 (Modo Local).
* **Lenguaje:** Python 3.12 con PySpark.
* **Java:** OpenJDK 11.

## 🚀 Instrucciones de Ejecución

1. Clona este repositorio o descarga el código fuente en tu máquina virtual.
2. Asegúrate de tener el archivo de datos nombrado como `datos.csv` en el mismo directorio del script.
3. Activa el entorno virtual del curso:
   ```bash
   source mi_entorno/bin/activate
