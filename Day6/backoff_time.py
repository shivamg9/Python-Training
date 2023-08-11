"""
Implement the retry mechanism in the task 1 (PhishTank) with backoff time for the fault tolerance of request. 

Use built-in “requests.packages.urllib3.util.retry.Retry” 

"""


import requests
import urllib3
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

def check_phishing_url(url):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    api_url = 'https://checkurl.phishtank.com/checkurl/index.php'

    data = {
        'url': url,
        'format': 'json',
        'app_key': '<PHISHTANK_APP_KEY>'
    }

    retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[429, 500, 502, 503, 504])
    session = requests.Session()
    session.mount('https://', HTTPAdapter(max_retries=retries))

    try:
        response = session.post(api_url, data=data, verify=False)
        json_response = response.json()

        if json_response['results']['in_database']:
            return f"{url} is a phishing URL."
        else:
            return f"{url} is not a phishing URL."

    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

def demo():
    url = input("Enter a URL to check for phishing: ")
    result = check_phishing_url(url)
    print(result)

demo()
