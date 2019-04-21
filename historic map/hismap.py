from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json
import os
app = Flask(__name__)

script_dir = os.path.dirname('hismap.py')
rel_path = "static\\question.json"
abs_file_path = os.path.join(script_dir, rel_path).replace("\\","/")
with open(abs_file_path) as json_file:
	qdata = json.load(json_file)

score = 0

@app.route('/')
def index():  
    return render_template('index.html') 

@app.route('/intelligence')
def map():
    return render_template('map.html') 

@app.route('/expedition')
def scout():
    return render_template('scout.html',qdata = qdata,score = score)

if __name__ == '__main__':
    app.run(debug = True)