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
page = 1

@app.route('/')
def index():  
	return render_template('index.html') 

@app.route('/intelligence')
def map():
	return render_template('map.html') 

@app.route('/expedition')
def scout():
	return render_template('scout.html',score=score,page=page)

@app.route('/answer_quiz', methods=['GET', 'POST'])
def answer_quiz():
	global qdata
	global score
	global page

	user_answer = request.get_json()
	index = page - 1
	correct_index = qdata[index]["Index"]
	if qdata[index]["Answer"] == user_answer:
		score += 10

	return jsonify(correct_index=correct_index,score=score)

@app.route('/display_questions', methods=['GET', 'POST'])
def display_questions():
	global qdata
	global page

	new_page = request.get_json()
	if new_page == 1:
		page += 1
	question = {
		"City": qdata[page - 1]["City"],
		"Question": qdata[page - 1]["Question"], 
		"Option1": qdata[page - 1]["Option1"],
		"Option2": qdata[page - 1]["Option2"],
		"Option3": qdata[page - 1]["Option3"],
		"Option4": qdata[page - 1]["Option4"]
	}

	return jsonify(question=question,page=page,score=score)

@app.route('/refresh', methods=['GET', 'POST'])
def refresh():
	global page
	global score

	if request.method == 'POST':
		page = 1
		score = 0

		return "Success"
	elif request.method == 'GET':
		return jsonify(score=score,page=page)
		
if __name__ == '__main__':
	app.run(debug = True)