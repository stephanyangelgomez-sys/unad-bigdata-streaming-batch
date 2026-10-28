# Proyecto Big Data: Procesamiento en Batch y Tiempo Real con Apache Kafka y Spark

Este proyecto implementa una solución completa que abarca el análisis estático en *batch* y el procesamiento continuo en tiempo real (streaming).

#  Tecnologías y Entorno
* **Sistema Operativo:** Ubuntu (VirtualBox VM)
* **Orquestación de Mensajes:** Apache ZooKeeper y Apache Kafka
* **Procesamiento Distribuido:** Apache Spark (Batch y Structured Streaming)
* **Lenguaje:** Python (PySpark)

---

#  Estructura del Repositorio

* `tarea3.py` (o `spark_batch_analysis.py`): Script de PySpark encargado del procesamiento y análisis en *batch* de los datos.
* `streaming/kafka_producer.py`: Simulador de eventos (sensores) que transmite mensajes en formato JSON hacia un tópico de Kafka.
* `streaming/spark_streaming_consumer.py`: Aplicación de Spark Structured Streaming que consume en tiempo real desde Kafka y calcula métricas en ventanas de tiempo.

---

#  Instrucciones de Ejecución

## 1. Ejecución del Procesamiento en Batch
Para ejecutar el script de análisis estático con Spark:
```bash
spark-submit tarea3.py
