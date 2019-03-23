from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

current_id = 4
sales = [
	{
		"id": 1,
		"salesperson": "James D. Halpert",
		"client": "Shake Shack",
		"reams": 1000
	},
	{
		"id": 2,
		"salesperson": "Stanley Hudson",
		"client": "Toast",
		"reams": 4000
	},
	{
		"id": 3,
		"salesperson": "Michael G. Scott",
		"client": "Computer Science Department",
		"reams": 10000
	},
]
clients = [
	"Shake Shack",
	"Toast",
	"Computer Science Department",
	"Teacher's College",
	"Starbucks",
	"Subsconsious",
	"Flat Top",
	"Joe's Coffee",
	"Max Caffe",
	"Nussbaum & Wu",
	"Taco Bell",
];

non_ppc_people = [
"Phyllis",
"Dwight",
"Oscar",
"Creed",
"Pam",
"Jim",
"Stanley",
"Michael",
"Kevin",
"Kelly"
]
ppc_people = [
"Angela"
]

@app.route('/infinity')
def infinity(name=None):
	return render_template('cu-paper-infinity.html', sales=sales, clients=clients)

@app.route('/ppc')
def ppc(name=None):
	return render_template('ppc.html', non_ppc_people=non_ppc_people, ppc_people=ppc_people)

@app.route('/save_sale', methods=['GET', 'POST'])
def save_sale():
	global current_id
	global sales
	global clients

	json_data = request.get_json()
	salesperson = json_data["salesperson"]
	client = json_data["client"]
	reams = json_data["reams"]

	current_id += 1
	new_sale_log = {
		"id":  current_id,
		"salesperson": salesperson,
		"client": client,
		"reams": reams
	}
	sales.append(new_sale_log)
	if client not in clients:
		clients.append(client)

	return jsonify(sales=sales, clients=clients)

@app.route('/delete_sale', methods=['GET', 'POST'])
def delete_sale():
	global sales

	delete_id = request.get_json()

	del sales[delete_id]

	return jsonify(sales=sales)

@app.route('/move_to_non_ppc', methods=['GET', 'POST'])
def move_to_non_ppc():
	global non_ppc_people
	global ppc_people

	name = request.get_json()

	if name not in non_ppc_people:
		non_ppc_people.append(name)
		ppc_people.remove(name)

	return jsonify(non_ppc_people=non_ppc_people, ppc_people=ppc_people)

@app.route('/move_to_ppc', methods=['GET', 'POST'])
def move_to_ppc():
	global non_ppc_people
	global ppc_people

	name = request.get_json()

	if name not in ppc_people:
		ppc_people.append(name)
		non_ppc_people.remove(name)

	return jsonify(non_ppc_people=non_ppc_people, ppc_people=ppc_people)


if __name__ == '__main__':
   app.run(debug = True)