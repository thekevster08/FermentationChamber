from flask import Flask, render_template, request, jsonify, send_from_directory 

import os
import SQLTools

app = Flask(__name__)
setpoint = 5

@app.route('/')
def main():
    return render_template('index.html')
    
@app.route('/new', methods=['POST'])
def start():
    SQLTools.drop_temperature_table()
    return "New Pressed"

@app.route('/save/', methods=['GET'])
def echo():
    filename = request.args.get('saveFilename')
    SQLTools.save_temperature_table(filename)
    ret_data = {"value": request.args.get('saveFilename')}
    return jsonify(ret_data)
    
@app.route('/load/', methods=['GET'])
def load():
    filename = request.args.get('loadFilename')
    SQLTools.load_temperature_table(filename)
    ret_data = {"value": request.args.get('loadFilename')}
    return jsonify(ret_data)
    
if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)