"""
Create a python module named "mapquest" for abstracting the interactions with Mapquest API.  
Implement a demo function which will utilize the functionality. 
Using separate module instead of direct requests will avoid duplicate code for handling exceptions,  
retry-mechanism, authentication, etc.  
And it will be easy to update code in future at only one place instead of in each file it is used. 
GeoCoding API: https://developer.mapquest.com/documentation/geocoding-api/ 
Getting Auth Key: https://developer.mapquest.com/user/me/apps 

Only following geocoding related endpoints needs to be integrated (GET and POST). 
- geocoding/v1/address 
- geocoding/v1/reverse 
- geocoding/v1/batch 

- Use request.Session(...) to avoid repetition of authentication or header setting etc. 
- Do appropriate logging in log file 
- Use retry mechanism 
- Use exception handling 

Usage: 
- import mapquest 
- client = mapquest.MapQuest(...) 
- response = client.get_address(...) 
- response = client.post_address(...) 
- response = client.get_reverse(...) 

Returns:    _type_: _description_
    \
"""

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import logging

class MapQuest:
    def __init__(self, auth_key):
        self.base_url = 'https://www.mapquestapi.com/geocoding/v1'
        self.auth_key = auth_key
        self.session = self.create_session()
        self.logger = self.setup_logger()

    def create_session(self):
        session = requests.Session()
        retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[429, 500, 502, 503, 504])
        session.mount('https://', HTTPAdapter(max_retries=retries))
        return session

    def setup_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler('mapquest.log')
        file_handler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger

    def get_address(self, location):
        endpoint = '/address'
        url = f"{self.base_url}{endpoint}"
        params = {
            'key': self.auth_key,
            'location': location
        }

        try:
            response = self.session.get(url, params=params)
            self.logger.info(f"GET Address: {url} - Status Code: {response.status_code}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"GET Address: {url} - Error: {str(e)}")
            return None

    def post_address(self, location):
        endpoint = '/address'
        url = f"{self.base_url}{endpoint}"
        params = {
            'key': self.auth_key
        }
        data = {
            'location': location
        }

        try:
            response = self.session.post(url, params=params, json=data)
            self.logger.info(f"POST Address: {url} - Status Code: {response.status_code}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"POST Address: {url} - Error: {str(e)}")
            return None

    def get_reverse(self, latitude, longitude):
        endpoint = '/reverse'
        url = f"{self.base_url}{endpoint}"
        params = {
            'key': self.auth_key,
            'location': f"{latitude},{longitude}"
        }

        try:
            response = self.session.get(url, params=params)
            self.logger.info(f"GET Reverse: {url} - Status Code: {response.status_code}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"GET Reverse: {url} - Error: {str(e)}")
            return None


import mapquest

client = mapquest.MapQuest('RAX0jxIbm8yd8YPr3GkzsYVhdwdKHMcF')

response = client.get_address('New York, USA')
print(response)

response = client.post_address('New York, USA')
print(response)

response = client.get_reverse(40.7128, -74.0060)
print(response)

"""
output:

{'info': {'statuscode': 0, 'copyright': {'text': '© 2023 MapQuest, Inc.', 'imageUrl': 'http://api.mqcdn.com/res/mqlogo.gif', 'imageAltText': '© 2023 MapQuest, Inc.'}, 'messages': []}, 'options': {'maxResults': -1, 'ignoreLatLngInput': False}, 'results': [{'providedLocation': {'location': 'New York, USA'}, 'locations': [{'street': '', 'adminArea6': '', 'adminArea6Type': 'Neighborhood', 'adminArea5': 'New York', 'adminArea5Type': 'City', 'adminArea4': 'New York', 'adminArea4Type': 'County', 'adminArea3': 'NY', 'adminArea3Type': 'State', 'adminArea1': 'US', 'adminArea1Type': 'Country', 'postalCode': '', 'geocodeQualityCode': 'A5XAX', 'geocodeQuality': 'CITY', 'dragPoint': False, 'sideOfStreet': 'N', 'linkId': '0', 'unknownInput': '', 'type': 's', 'latLng': {'lat': 40.71453, 'lng': -74.00712}, 'displayLatLng': {'lat': 40.71453, 'lng': -74.00712}, 'mapUrl': ''}, {'street': '', 'adminArea6': '', 'adminArea6Type': 'Neighborhood', 'adminArea5': '', 'adminArea5Type': 'City', 'adminArea4': '', 'adminArea4Type': 'County', 'adminArea3': 'NY', 'adminArea3Type': 'State', 'adminArea1': 'US', 'adminArea1Type': 'Country', 'postalCode': '', 'geocodeQualityCode': 'A3XAX', 'geocodeQuality': 'STATE', 'dragPoint': False, 'sideOfStreet': 'N', 'linkId': '0', 'unknownInput': '', 'type': 's', 'latLng': {'lat': 42.65155, 'lng': -73.75522}, 'displayLatLng': {'lat': 42.65155, 'lng': -73.75522}, 'mapUrl': ''}]}]}
{'info': {'statuscode': 0, 'copyright': {'text': '© 2023 MapQuest, Inc.', 'imageUrl': 'http://api.mqcdn.com/res/mqlogo.gif', 'imageAltText': '© 2023 MapQuest, Inc.'}, 'messages': []}, 'options': {'maxResults': -1, 'ignoreLatLngInput': False}, 'results': [{'providedLocation': {'street': 'New York, USA'}, 'locations': [{'street': '', 'adminArea6': '', 'adminArea6Type': 'Neighborhood', 'adminArea5': 'New York', 'adminArea5Type': 'City', 'adminArea4': 'New York', 'adminArea4Type': 'County', 'adminArea3': 'NY', 'adminArea3Type': 'State', 'adminArea1': 'US', 'adminArea1Type': 'Country', 'postalCode': '', 'geocodeQualityCode': 'A5XAX', 'geocodeQuality': 'CITY', 'dragPoint': False, 'sideOfStreet': 'N', 'linkId': '0', 'unknownInput': '', 'type': 's', 'latLng': {'lat': 40.71453, 'lng': -74.00712}, 'displayLatLng': {'lat': 40.71453, 'lng': -74.00712}, 'mapUrl': ''}, {'street': '', 'adminArea6': '', 'adminArea6Type': 'Neighborhood', 'adminArea5': '', 'adminArea5Type': 'City', 'adminArea4': '', 'adminArea4Type': 'County', 'adminArea3': 'NY', 'adminArea3Type': 'State', 'adminArea1': 'US', 'adminArea1Type': 'Country', 'postalCode': '', 'geocodeQualityCode': 'A3XAX', 'geocodeQuality': 'STATE', 'dragPoint': False, 'sideOfStreet': 'N', 'linkId': '0', 'unknownInput': '', 'type': 's', 'latLng': {'lat': 42.65155, 'lng': -73.75522}, 'displayLatLng': {'lat': 42.65155, 'lng': -73.75522}, 'mapUrl': ''}]}]}
{'info': {'statuscode': 0, 'copyright': {'text': '© 2023 MapQuest, Inc.', 'imageUrl': 'http://api.mqcdn.com/res/mqlogo.gif', 'imageAltText': '© 2023 MapQuest, Inc.'}, 'messages': []}, 'options': {'maxResults': 1, 'ignoreLatLngInput': False}, 'results': [{'providedLocation': {'latLng': {'lat': 40.7128, 'lng': -74.006}}, 'locations': [{'street': 'Centre St', 'adminArea6': 'Civic Center', 'adminArea6Type': 'Neighborhood', 'adminArea5': 'New York', 'adminArea5Type': 'City', 'adminArea4': 'New York', 'adminArea4Type': 'County', 'adminArea3': 'NY', 'adminArea3Type': 'State', 'adminArea1': 'US', 'adminArea1Type': 'Country', 'postalCode': '10007', 'geocodeQualityCode': 'P1AAA', 'geocodeQuality': 'POINT', 'dragPoint': False, 'sideOfStreet': 'L', 'linkId': '0', 'unknownInput': '', 'type': 's', 'latLng': {'lat': 40.7122, 'lng': -74.00545}, 'displayLatLng': {'lat': 40.71278, 'lng': -74.00594}, 'mapUrl': ''}]}]}
{'info': {'statuscode': 0, 'copyright': {'text': '© 2023 MapQuest, Inc.', 'imageUrl': 'http://api.mqcdn.com/res/mqlogo.gif', 'imageAltText': '© 2023 MapQuest, Inc.'}, 'messages': []}, 'options': {'maxResults': -1, 'ignoreLatLngInput': False}, 'results': [{'providedLocation': {'location': 'New York, USA'}, 'locations': [{'street': '', 'adminArea6': '', 'adminArea6Type': 'Neighborhood', 'adminArea5': 'New York', 'adminArea5Type': 'City', 'adminArea4': 'New York', 'adminArea4Type': 'County', 'adminArea3': 'NY', 'adminArea3Type': 'State', 'adminArea1': 'US', 'adminArea1Type': 'Country', 'postalCode': '', 'geocodeQualityCode': 'A5XAX', 'geocodeQuality': 'CITY', 'dragPoint': False, 'sideOfStreet': 'N', 'linkId': '0', 'unknownInput': '', 'type': 's', 'latLng': {'lat': 40.71453, 'lng': -74.00712}, 'displayLatLng': {'lat': 40.71453, 'lng': -74.00712}, 'mapUrl': ''}, {'street': '', 'adminArea6': '', 'adminArea6Type': 'Neighborhood', 'adminArea5': '', 'adminArea5Type': 'City', 'adminArea4': '', 'adminArea4Type': 'County', 'adminArea3': 'NY', 'adminArea3Type': 'State', 'adminArea1': 'US', 'adminArea1Type': 'Country', 'postalCode': '', 'geocodeQualityCode': 'A3XAX', 'geocodeQuality': 'STATE', 'dragPoint': False, 'sideOfStreet': 'N', 'linkId': '0', 'unknownInput': '', 'type': 's', 'latLng': {'lat': 42.65155, 'lng': -73.75522}, 'displayLatLng': {'lat': 42.65155, 'lng': -73.75522}, 'mapUrl': ''}]}]}
{'info': {'statuscode': 0, 'copyright': {'text': '© 2023 MapQuest, Inc.', 'imageUrl': 'http://api.mqcdn.com/res/mqlogo.gif', 'imageAltText': '© 2023 MapQuest, Inc.'}, 'messages': []}, 'options': {'maxResults': -1, 'ignoreLatLngInput': False}, 'results': [{'providedLocation': {'street': 'New York, USA'}, 'locations': [{'street': '', 'adminArea6': '', 'adminArea6Type': 'Neighborhood', 'adminArea5': 'New York', 'adminArea5Type': 'City', 'adminArea4': 'New York', 'adminArea4Type': 'County', 'adminArea3': 'NY', 'adminArea3Type': 'State', 'adminArea1': 'US', 'adminArea1Type': 'Country', 'postalCode': '', 'geocodeQualityCode': 'A5XAX', 'geocodeQuality': 'CITY', 'dragPoint': False, 'sideOfStreet': 'N', 'linkId': '0', 'unknownInput': '', 'type': 's', 'latLng': {'lat': 40.71453, 'lng': -74.00712}, 'displayLatLng': {'lat': 40.71453, 'lng': -74.00712}, 'mapUrl': ''}, {'street': '', 'adminArea6': '', 'adminArea6Type': 'Neighborhood', 'adminArea5': '', 'adminArea5Type': 'City', 'adminArea4': '', 'adminArea4Type': 'County', 'adminArea3': 'NY', 'adminArea3Type': 'State', 'adminArea1': 'US', 'adminArea1Type': 'Country', 'postalCode': '', 'geocodeQualityCode': 'A3XAX', 'geocodeQuality': 'STATE', 'dragPoint': False, 'sideOfStreet': 'N', 'linkId': '0', 'unknownInput': '', 'type': 's', 'latLng': {'lat': 42.65155, 'lng': -73.75522}, 'displayLatLng': {'lat': 42.65155, 'lng': -73.75522}, 'mapUrl': ''}]}]}
{'info': {'statuscode': 0, 'copyright': {'text': '© 2023 MapQuest, Inc.', 'imageUrl': 'http://api.mqcdn.com/res/mqlogo.gif', 'imageAltText': '© 2023 MapQuest, Inc.'}, 'messages': []}, 'options': {'maxResults': 1, 'ignoreLatLngInput': False}, 'results': [{'providedLocation': {'latLng': {'lat': 40.7128, 'lng': -74.006}}, 'locations': [{'street': 'Centre St', 'adminArea6': 'Civic Center', 'adminArea6Type': 'Neighborhood', 'adminArea5': 'New York', 'adminArea5Type': 'City', 'adminArea4': 'New York', 'adminArea4Type': 'County', 'adminArea3': 'NY', 'adminArea3Type': 'State', 'adminArea1': 'US', 'adminArea1Type': 'Country', 'postalCode': '10007', 'geocodeQualityCode': 'P1AAA', 'geocodeQuality': 'POINT', 'dragPoint': False, 'sideOfStreet': 'L', 'linkId': '0', 'unknownInput': '', 'type': 's', 'latLng': {'lat': 40.7122, 'lng': -74.00545}, 'displayLatLng': {'lat': 40.71278, 'lng': -74.00594}, 'mapUrl': ''}]}]}

"""