from flask import Flask, jsonify, request
from prettytable import PrettyTable
import json, requests

###### api.py
#   Coding challenge for Lightfeather
#   @author Joseph Ashley <joseph.ashley@protonmail.com>
#   @date   2021-09-16
######

app = Flask(__name__)

### Returns formatted list of supervisors
@app.route("/api/supervisors", methods=["GET"])
def getSupervisors():
    raw_list = requests.get('https://609aae2c0f5a13001721bb02.mockapi.io/lightfeather/managers')
    sorted_list = test_sort(raw_list.json())
    return jsonify(sorted_list)

# Sort alphabetically by jurisdiction, last name, then first name.
# Do not return entries with numerical jurisdictions.
def test_sort(raw_list):
    tmp_list = sorted(raw_list, key=lambda k: (k['jurisdiction'], k['lastName'], k['firstName']))
    sorted_list = []
    for item in tmp_list:
        if not item['jurisdiction'].isdigit():
            formatted_str = item['jurisdiction']+" - "+item['lastName']+", "+item['firstName']
            sorted_list.append(formatted_str)
    return sorted_list

### Accepts a submission of contact and supervisor info.
@app.route("/api/submit", methods=["POST"])
def submitInfo():

    # Parse data
    firstName = request.json['firstName']
    lastName = request.json['lastName']
    supervisor = request.json['supervisor']
    contactMethod = request.json['contactMethod']
    email = request.json['email']
    phone = request.json['phone']
    
    # Prepare for display
    info = {
        'firstName': firstName,
        'lastName': lastName,
        'email': email,
        'phone': phone,
        'supervisor': supervisor,
        'contactMethod': contactMethod
        }
    email_flag = "* " if contactMethod == "Email" else '  ' 
    phone_flag = "* " if contactMethod == "Phone" else '  '
    info_txt = "\n\n" + "Information submitted successfully." + "\n\n" \
        + "    First Name: "+firstName+"\n" \
        + "    Last Name: "+lastName+"\n" \
        + "  " + email_flag +"Email: "+email+"\n" \
        + "  " + phone_flag + "Phone: "+phone+"\n" \
        + "    Supervisor: "+supervisor+"\n"

    # Return information to user
    print(info_txt)
    return jsonify(info)


if __name__ == '__main__':
    app.run(port=8080)

