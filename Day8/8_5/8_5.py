import requests
import json
import logging
from concurrent.futures import ThreadPoolExecutor
import threading

output_file_lock = threading.Lock()

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

        # Append to output.json using file locking
        with output_file_lock:
            with open('output.json', 'a') as output_file:
                json.dump(location_info, output_file)
                output_file.write('\n')

def main():
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
