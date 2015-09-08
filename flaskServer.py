from flask import Flask, render_template, request 

import os
import collectDataSim
import recordJSON

app = Flask(__name__)
app.debug = True

setpoint = 5

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/interface',methods=['POST'])
def interface():
    return "this is the return message"
    

@app.route('/setSetpoint', methods=['POST'])
def setSetpoint():
    
    #_setpoint = request.form['setpoint']
    return "button hit"
    # setpoint = _setpoint
    # return setpoint

@app.route('/update_setpoint/', methods=['POST'])
def hello():
    setpoint=request.form['setpoint']
    return render_template('index.html', setpoint=setpoint)


def collect_data():
    collectDataSim.collect_data()
    recordJSON.record_JSON

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)