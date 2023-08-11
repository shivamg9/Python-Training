"""
Create a simple API Web Server (using flask) similar to PhishTank API service.  
PhishTank is a free online service, which stores information about Phishing URLs. 
It should have one POST endpoint named "checkurl" which accepts the following Request Body Parameters  
and returns the response with following Response Fields.  

Implement a demo function which will utilize the functionality 

Request Body Parameter: 
- url: encoded url 
- format: “json” | “xml” 


Response Fields: 
- url: URL passed in input 
- is_valid: yes | no | unknown 

Server will have one static hard-coded csv file with two columns "url" and "is_valid".  
For each request, check if csv file contains entry for that url,  
if yes then return is_valid field accordingly else return is_valid as unknown. 

Sample CSV File: 
url, is_valid 
https://google.com, yes 
https://dummy.com, no 

PhishTank API: https://www.phishtank.com/api_info.php 
"""

from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

csv_file = 'phishing_urls.csv'
phishing_urls = {}

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        phishing_urls[row['url']] = row['is_valid']

@app.route('/checkurl', methods=['GET', 'POST'])
def check_url():
    if request.method == 'POST':
        request_data = request.get_json()

        url = request_data.get('url')
        format_type = request_data.get('format', 'json')

        if url in phishing_urls:
            is_valid = phishing_urls[url]
        else:
            is_valid = 'unknown'

        response_data = {
            'url': url,
            'is_valid': is_valid
        }

        if format_type == 'xml':
            response = '<response><url>{}</url><is_valid>{}</is_valid></response>'.format(url, is_valid)
            return response, 200, {'Content-Type': 'application/xml'}
        else:
            return jsonify(response_data), 200

    elif request.method == 'GET':
        return "This is a GET request to /checkurl"

    return "Method Not Allowed", 405

def demo():
    app.run(port=8000)

demo()
