from flask import Flask, render_template, request, jsonify, send_from_directory 

import os
import SQLTools
import TempController
import collectDataSimThread
import configTools
import OutputTools
#import collectDataSim


#app = Flask(__name__, static_folder='var/www/FermentationChamber/FermentationChamber/static')
app = Flask(__name__)
app.debug = True
CDataThread = collectDataSimThread.CollectDataThread(1, "collectDataThread-1", 1)
CTemperatureThread = TempController.Controller(1, "controlTemperatureThread-1", 1)
#tempController = TempController.Controller(1, "Temperature Controller", 1)

# @app.route('/static/<path:filename>')
# def serve_static(filename):
#     root_dir = os.path.dirname(os.getcwd())
#     return send_from_directory(os.path.join(root_dir, 'statics'), filename)

@app.route('/')
def main():
    return render_template('index.html')
    
@app.route('/clear', methods=['POST'])
def start():
    SQLTools.drop_temperature_table()
    return "Clear Pressed"
    
@app.route('/startCollection', methods=['POST'])
def startCollection():
    CDataThread.unpause()
    return "Start Collection Pressed"
    
@app.route('/stopCollection', methods=['POST'])
def stopCollection():
    CDataThread.pause()
    return "Stop Collection Pressed"
    
@app.route('/startControl', methods=['POST'])
def startControl():
    CTemperatureThread.unpause()
    return "Start Control Pressed"
    
@app.route('/stopControl', methods=['POST'])
def stopControl():
    CTemperatureThread.pause()
    return "Stop Control Pressed"
    
@app.route('/coolOn', methods=['POST'])
def coolOn():
    OutputTools.coldOn()
    return "cool on Pressed"
    
@app.route('/coolOff', methods=['POST'])
def coolOff():
    OutputTools.coldOff()
    return "Start Control Pressed"
    
@app.route('/heatOn', methods=['POST'])
def heatOn():
    OutputTools.heatOn()
    return "Start Control Pressed"
    
@app.route('/heatOff', methods=['POST'])
def heatOff():
    OutputTools.heatOff()
    return "Start Control Pressed"

@app.route('/save/', methods=['GET'])
def echo():
    filename = request.args.get('saveFilename')
    SQLTools.save_temperature_table(filename)
#     return "asdf"
    ret_data = {"value": request.args.get('saveFilename')}
    return jsonify(ret_data)
    
@app.route('/load/', methods=['GET'])
def load():
    filename = request.args.get('loadFilename')
    SQLTools.load_temperature_table(filename)
#     return "asdf"
    ret_data = {"value": request.args.get('loadFilename')}
    return jsonify(ret_data)
    
@app.route('/updateSampleTime', methods=['GET'])
def updateSampleTime():
    sampleTime = request.args.get('sampleTime')
    configTools.updateSampleTime(sampleTime)
#     return "asdf"
    ret_data = {"value": request.args.get('sampleTime')}
    return jsonify(ret_data)
    
@app.route('/updateSetpoint', methods=['GET'])
def updateSetpoint():
    setpoint = request.args.get('setpoint')
    configTools.updateSetpoint(setpoint)
    return "Setpoint  Updated"
    
@app.route('/updateActiveDeadband', methods=['GET'])
def updateActiveDeadband():
    activeDeadband = request.args.get('activeDeadband')
    configTools.updateActiveDeadband(activeDeadband)
    return "Active Deadband Updated"
    
@app.route('/updateInactiveDeadband', methods=['GET'])
def updateInactiveDeadband():
    inactiveDeadband = request.args.get('inactiveDeadband')
    configTools.updateInactiveDeadband(inactiveDeadband)
    return "Inactive Deadband Updated"
    
if __name__ == '__init__':
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)