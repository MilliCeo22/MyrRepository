# Databricks notebook source
# MAGIC %sql
# MAGIC Describe default.rssi_data_from_gss

# COMMAND ----------

# MAGIC %sql
# MAGIC Select max(event_timestamp) from default.rssi_data_from_gss
# MAGIC --Where vin = 'HCCZ8405VMCN28985'
# MAGIC --Order by Network_ desc

# COMMAND ----------

# MAGIC %sql
# MAGIC Select max(event_date) from default.rssi_data_from_gss_filtered

# COMMAND ----------


