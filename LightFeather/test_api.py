from flask import Flask, jsonify, request
import json, requests

app = Flask(__name__)

@app.route("/api/supervisors", methods=["GET"])
def getSupervisors():
    raw_list = requests.get('https://609aae2c0f5a13001721bb02.mockapi.io/lightfeather/managers')
    sorted_list = test_sort(raw_list.json())
    return jsonify(sorted_list)

def test_sort(raw_list):
    # Sort alphabetically by jurisdiction, last name, then first name.
    # Do not return entries with numerical jurisdictions.
    tmp_list = sorted(raw_list, key=lambda k: (k['jurisdiction'], k['lastName'], k['firstName']))
    sorted_list = []
    for item in tmp_list:
        if not item['jurisdiction'].isdigit():
            formatted_str = item['jurisdiction']+" - "+item['lastName']+", "+item['firstName']
            sorted_list.append(formatted_str)
    #sorted_list = [item['jurisdiction']+" - "+item['lastName']+", "+item['firstName'] for item in tmp_list if ~(item['jurisdiction'].isdigit())]
    return sorted_list

@app.route("/api/submit", methods=["POST"])
def submitInfo():

    #print(request)

    # Parse data
    firstName = request.json['firstName']
    lastName = request.json['lastName']
    supervisor = request.json['supervisor']
    #contactMethod = request.json['contactMethod']
    email = request.json['email']
    phone = request.json['phone']
    #contactInfo = email if contactMethod == "Email" else phone

    
    # Prepare for display
    info = {
        'firstName': firstName,
        'lastName': lastName,
        'email': email,
        'phone': phone,
        'supervisor': supervisor
        }
    print(info)
    return jsonify(info)








@app.route("/accounts", methods=["GET"])
def getAccounts():
    return jsonify(accounts)

@app.route("/account/<id>", methods=["GET"])
def getAccount(id):
    id = int(id)-1
    return jsonify(accounts[id])

@app.route("/account", methods=["POST"])
def addAccount():
    name = request.json['name']
    balance = request.json['balance']
    data = {'name': name, 'balance': balance}
    accounts.append(data)
    return jsonify(data)




if __name__ == '__main__':
    app.run(port=8080)

