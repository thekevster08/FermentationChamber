Databases
-temperatures.db
-temperatures.json

static


templates
-index.html
-fermchamber.html
-interfacePage.html

python scripts
-collectDataScript.py
-recordJSONScript.py

server
-flaskServer.py

libraries
-


Milestones

fill in text box, click button, server reads it and sends back message. 
text gets updated with the response


Instructions for use:
-collectdata.py must be running to log data.
-flaskServer must be running to 

Feature Request
-add "start collection" button
-add "clearn db" button
-have start stop pause collection. have a green light indicating collection
-update constantly
    -its really not feasable to have it updating constantly, so lets not worry about that
-want to be able to save a current database, then load another one
-buttons: New, Start, Pause
-in plotChart instead of running getJSON, make a call to a function to copy everything from 
    the db to the json file, then call json
-have a start collection and stop collection button. only run the collect script of asked

Version Updates
-server working
-make sure that any files you need to access are in static (dumb)

