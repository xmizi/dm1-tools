# dm1-tools
* **ns-downloader.py**: my 1st attempt to collect data from NIghtscout API (I'm not using it. For upload to influxDB are needed mqtt and mqtt2influx)
* **node-red-nightscout.json**: actual way for collecting data - flow for Node-red. Data are uploaded to influxdb directly
* **nightscout-grafana.json**: nightscout dashboard for Grafana. Data stored in influxDB.
# note
Because I generate statistics for multiple people, I have defined an "id" (=person's name). Names are hardcoded in grafana variables. But it is not mandatory. If the stats are generated for only one person, just delete the variable.
