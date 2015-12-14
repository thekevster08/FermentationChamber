from flask import Flask, render_template, request, jsonify 

import os
import SQLTools
#import collectDataSim
# import collectDataSim
# import recordJSON

app = Flask(__name__)
app.debug = True

setpoint = 5

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/interface',methods=['POST'])
def interface():
    return "this is the return message"
    
@app.route('/start', methods=['POST'])
def start():
    SQLTools.drop_temperature_table()
    return "asdf"
    
    
@app.route('/setSetpoint', methods=['POST'])
def setSetpoint():
    
    #_setpoint = request.form['setpoint']
    return "button hit"
    # setpoint = _setpoint
    # return setpoint

# @app.route('/getData',methods=['GET'])
# def getData():
#     return "this is the return message"

@app.route('/update_setpoint/', methods=['POST'])
def hello():
    setpoint=request.form['setpoint']
    return render_template('index.html', setpoint=setpoint)


# def collect_data():
#     collectDataSim.collect_data()
#     recordJSON.record_JSON

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
    
if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)