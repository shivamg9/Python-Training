"""
Write a python program using "requests" (3rdparty) and "urllib3" (in-built) module to integrate "PhishTank" service.  
PhishTank is a free online service, which stores information about Phishing URLs. 
The Input to the program should be a URL. The output should tell us whether the input url is Phishing URL or not. 

Implement a demo function which will utilize the functionality. 
 
Input: http://www.travelswitchfly.com/ 	 
Output: "http://www.travelswitchfly.com/" is a phishing URL.  
PhishTank API - https://www.phishtank.com/api_info.php 
POST Endpoint - https://checkurl.phishtank.com/checkurl/index.php 

"""
    
import requests
import urllib3

def check_phishing_url(url):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    api_url = 'https://checkurl.phishtank.com/checkurl/index.php'
    params = {
        'url': url,
        'format': 'json',
        'app_key': 'PHISHTANK_API_KEY'
    }

    response = requests.post(api_url, data=params, verify=False)
    data = response.json()

    if data['results']['valid'] == 'true':
        return f"{url} is a phishing URL."
    else:
        return f"{url} is not a phishing URL."

def demo():
    url = input("Enter a URL to check if it is a phishing URL: ")
    result = check_phishing_url(url)
    print(result)


demo()

