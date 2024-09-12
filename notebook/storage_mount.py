{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "554d48f5-210d-41a2-8401-274c99604d6f",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "configs = {\n",
    "  \"fs.azure.account.auth.type\": \"CustomAccessToken\",\n",
    "  \"fs.azure.account.custom.token.provider.class\": spark.conf.get(\"spark.databricks.passthrough.adls.gen2.tokenProviderClassName\")\n",
    "}\n",
    "\n",
    "# Optionally, you can add <directory-name> to the source URI of your mount point.\n",
    "dbutils.fs.mount(\n",
    "  source = \"abfss://bronze@tokyoolympicdata24.dfs.core.windows.net/\",\n",
    "  mount_point = \"/mnt/bronze\",\n",
    "  extra_configs = configs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "8b1dd319-712d-4c1c-867e-986cc7bb0ddb",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "dbutils.fs.ls(\"/mnt/bronze/SalesLT\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "da89beb5-e476-4160-a1bf-1081689957cc",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "configs = {\n",
    "  \"fs.azure.account.auth.type\": \"CustomAccessToken\",\n",
    "  \"fs.azure.account.custom.token.provider.class\": spark.conf.get(\"spark.databricks.passthrough.adls.gen2.tokenProviderClassName\")\n",
    "}\n",
    "\n",
    "# Optionally, you can add <directory-name> to the source URI of your mount point.\n",
    "dbutils.fs.mount(\n",
    "  source = \"abfss://silver@tokyoolympicdata24.dfs.core.windows.net/\",\n",
    "  mount_point = \"/mnt/silver\",\n",
    "  extra_configs = configs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {},
     "inputWidgets": {},
     "nuid": "64c7784d-897a-4ee9-87ed-53d16496eb63",
     "showTitle": false,
     "title": ""
    }
   },
   "outputs": [],
   "source": [
    "configs = {\n",
    "  \"fs.azure.account.auth.type\": \"CustomAccessToken\",\n",
    "  \"fs.azure.account.custom.token.provider.class\": spark.conf.get(\"spark.databricks.passthrough.adls.gen2.tokenProviderClassName\")\n",
    "}\n",
    "\n",
    "# Optionally, you can add <directory-name> to the source URI of your mount point.\n",
    "dbutils.fs.mount(\n",
    "  source = \"abfss://gold@tokyoolympicdata24.dfs.core.windows.net/\",\n",
    "  mount_point = \"/mnt/gold\",\n",
    "  extra_configs = configs)"
   ]
  }
 ],
 "metadata": {
  "application/vnd.databricks.v1+notebook": {
   "dashboards": [],
   "environmentMetadata": null,
   "language": "python",
   "notebookMetadata": {},
   "notebookName": "storage_mount",
   "widgets": {}
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
