**Problem:** We store files on your local device and process them using languages like R and Python. However, local workstations are limited and cannot handle massive datasets. 
**Solution:** **Distributed processing** is a setup in which multiple processors are used to run an application. Instead of processing large datasets on a single computer, the task can be divided between various devices that communicate 

**What is Apache Spark?**

Apache Spark is a distributed processing system for big data and machine learning tasks on large datasets. It enables users to run queries and workflows on petabytes of data, outperforming previous engines like Hadoop. Major companies like IBM, Amazon, and Yahoo use Apache Spark.

**What is PySpark?**

PySpark is the Python interface for Apache Spark. It allows users to write Python and SQL-like commands to manipulate and analyze data in a distributed environment. Data scientists use PySpark to manage data, build machine learning pipelines, and tune models.

**Why Use PySpark?**
1. Speed: PySpark processes big data faster than Pandas and Dask, handling petabytes of data efficiently.
2. Real-time Data: Unlike Hadoop's batch processing, PySpark can handle real-time data collection.
3. Community Support: Spark has better community support and reliability compared to Apache Flink.
4. Fault Tolerance: PySpark can recover from failures and supports in-memory computation, running even without a hard drive or SSD.

We are going to perform ETL (Extract Load Transform) on [this]([url](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410001701)) dataset taken from statistics canada. 
**Overview of the Dataset**
The dataset contains employment statistics for Canada, segmented by various age groups and gender. Here are the key columns in the dataset:

REF_DATE: The reference date for the data (e.g., "2024-11").
GEO: The geographical area, which is "Canada" in this dataset.
Labour force characteristics: This column indicates the type of labour force data, which is "Employment" in this case.
Gender: The gender category, including "Total - Gender", "Men+", and "Women+".
Age group: The age group of the individuals (e.g., "15 years and over", "15 to 24 years").
UOM: Unit of measure, which is "Persons in thousands."
VALUE: The actual employment numbers.
