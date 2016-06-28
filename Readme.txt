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

Installation Instructions:
-Install - 
    *navigate to /var/www/FermentationChamber/FermentationChamber
    *git fetch --all
    *git reset --hard origin/master
-Set Permissions -
    *navigate to ./static
    *sudo chmod 777 temperatures.json
    *sudo chmod 777 temperatures.db
    *sudo chown www-data temperatures.db
    *sudo chown www-data temperatures.json
    *sudo chgrp wwwdatapi temperatures.db
    *sudo chgrp wwwdatapi temperatures.json

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



to return from dev to release on PID
rename main.py to __init__.py
rename the if __main__ to if __init_)_
update file paths in SQLTools.py (had to break all of them)



this version user stories:



future version user stories:
-be able to control to either fridge temp or beer temp
-have manual output for heat and cold
-clean up checkboxes
-save checkbox visibility