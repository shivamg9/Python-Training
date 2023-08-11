"""
Add multithreading support for API call in handson of REST, (parsing info from Mapquest API) 

a.Get latitude and longitude list from https://dpaste.com/F9VQFPJED.txt using GET call. 

Each line, 

Lat,lon 

lat,lon 

b.For each entry in above list get information of street, city, country, postalcode etc. 

c.Store parsed information of each record in diff file. ex. Filename: 		  	<		<street>_<postalcode>.json 

d.Add loggers in and save log in log.log file.reference: https://developer.mapquest.com/documentation/samples/geocoding/v1/reverse/ 
 
"""


import requests
import json
import logging
from concurrent.futures import ThreadPoolExecutor

def get_lat_lon_list(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.splitlines()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to get latitude and longitude list: {str(e)}")
        return None


def get_location_info(lat, lon):
    api_key = 'RAX0jxIbm8yd8YPr3GkzsYVhdwdKHMcF'  # Replace with your actual Mapquest API key
    url = f'https://www.mapquestapi.com/geocoding/v1/reverse?key={api_key}&location={lat},{lon}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def process_location(lat, lon):
    location_info = get_location_info(lat, lon)
    if location_info:
        street = location_info['results'][0]['locations'][0]['street']
        postalcode = location_info['results'][0]['locations'][0]['postalCode']
        filename = f"{street}_{postalcode}.json"
        with open(filename, 'w') as file:
            json.dump(location_info, file)

def main():
    # Sample latitude and longitude list for testing
    lat_lon_list = [
        "40.7128,-74.0060",
        "34.0522,-118.2437",
        "41.8781,-87.6298",
        # Add more latitude and longitude pairs as needed
    ]

    if not lat_lon_list:
        print("Failed to get latitude and longitude list.")
        return

    # Configure logger
    logging.basicConfig(filename='log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()

    with ThreadPoolExecutor() as executor:
        futures = []
        for lat_lon in lat_lon_list:
            lat, lon = lat_lon.strip().split(',')
            futures.append(executor.submit(process_location, lat, lon))

        for future in futures:
            try:
                future.result()
            except Exception as e:
                logger.error(f"Error occurred: {str(e)}")

if __name__ == '__main__':
    main()
