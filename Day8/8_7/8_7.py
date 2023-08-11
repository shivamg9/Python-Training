import requests
import json
import logging
from concurrent.futures import ProcessPoolExecutor
import os
import queue
import multiprocessing

MAX_PROCESSES_API_CALL = 3
MAX_PROCESSES_FILE_WRITE = 2

output_file_lock = multiprocessing.Lock()
lat_lon_list = queue.Queue()
output_queue = multiprocessing.Queue()

def get_location_info(lat, lon):
    api_key = 'RAX0jxIbm8yd8YPr3GkzsYVhdwdKHMcF'  # Replace with your actual Mapquest API key
    url = f'https://www.mapquestapi.com/geocoding/v1/reverse?key={api_key}&location={lat},{lon}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def process_location():
    while not lat_lon_list.empty():
        lat_lon = lat_lon_list.get()
        lat, lon = lat_lon.strip().split(',')
        location_info = get_location_info(lat, lon)
        if location_info:
            output_queue.put(location_info)

def write_to_file():
    while not output_queue.empty():
        location_info = output_queue.get()
        street = location_info['results'][0]['locations'][0]['street']
        postalcode = location_info['results'][0]['locations'][0]['postalCode']
        filename = f"{street}_{postalcode}.json"
        with open(filename, 'w') as file:
            json.dump(location_info, file)
            file.write('\n')

def main():
    lat_lon_list.put("40.7128,-74.0060")
    lat_lon_list.put("34.0522,-118.2437")
    lat_lon_list.put("41.8781,-87.6298")
    # Add more latitude and longitude pairs as needed

    # Configure logger
    logging.basicConfig(filename='log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()

    # Create ProcessPoolExecutor for API calls
    with ProcessPoolExecutor(max_workers=MAX_PROCESSES_API_CALL) as api_executor:
        api_futures = [api_executor.submit(process_location) for _ in range(MAX_PROCESSES_API_CALL)]

    # Create ProcessPoolExecutor for file writing
    with ProcessPoolExecutor(max_workers=MAX_PROCESSES_FILE_WRITE) as file_executor:
        file_futures = [file_executor.submit(write_to_file) for _ in range(MAX_PROCESSES_FILE_WRITE)]

    for api_future in api_futures:
        try:
            api_future.result()
        except Exception as e:
            logger.error(f"API Call Error occurred: {str(e)}")

    for file_future in file_futures:
        try:
            file_future.result()
        except Exception as e:
            logger.error(f"File Write Error occurred: {str(e)}")

if __name__ == '__main__':
    main()
