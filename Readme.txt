Fermentation Chamber
version -1.00
A simple fermentation chamber control center.

Features:
Plots data from 3 GPIO pins. Can create a new database, save the current database as an external file, or load a previous database.

Instructions for use:
-The flask server must be running to respond to http requests. Start flaskServer.py with the following command:
    >> python flaskServer.py
-A collect data script must be running to populate the database with data. Start collectData.py with the following command:
    >> python collectData.py


Version Notes:

Feature Request
Data collection control:
    -Add the following buttons: "start collection", "stop collection"
    -Have a green light indicating data is being collected.
    -In plotChart instead of running getJSON, make a call to a function to copy everything from 
        the db to the json file, then call json. This way you don't have to constantly rewrite the 
        JSON database. This would be a huge performance boost.

Stretch goals:
-update constantly
    -its really not feasable to have it updating constantly, so lets not worry about that
    
Known Bugs:
-you need to have a seperate script always running seperate of the data collection to dump 
    to JSON. if you load something while its not running you are not going to get any json 
    data.

