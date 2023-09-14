# dm1-tools
* '''ns-checker.py''': my 1st attempt to collect data from NIghtscout API (I'm not using it)
* '''node-red-nightscout.json''' actual way for collecting data - flow for Node-red. Because I have co 
* nightascout-grafana.json: nightscout dashboard for Grafana. Data stored in influxDB.

Because I generate statistics for multiple people, I have defined an "id" (=person's name). It is not mandatory - I have it hardcoded in variables. If the stats are generated for only one person, just delete the variable. (id is also defined in flow node red)
