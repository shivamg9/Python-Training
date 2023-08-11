import requests
import json
import logging
from concurrent.futures import ThreadPoolExecutor
import threading
import os
import queue

MAX_THREADS_API_CALL = 5
MAX_THREADS_FILE_WRITE = 2

output_file_lock = threading.Lock()
lat_lon_list = queue.Queue()
output_list = queue.Queue()

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
            output_list.put(location_info)

def write_to_file():
    with output_file_lock:
        if not os.path.exists('output.json'):
            with open('output.json', 'w') as output_file:
                pass  # Create the file if it doesn't exist

        with open('output.json', 'a') as output_file:
            while not output_list.empty():
                location_info = output_list.get()
                json.dump(location_info, output_file)
                output_file.write('\n')

def main():
    lat_lon_list.put("40.7128,-74.0060")
    lat_lon_list.put("34.0522,-118.2437")
    lat_lon_list.put("41.8781,-87.6298")
    # Add more latitude and longitude pairs as needed

    # Configure logger
    logging.basicConfig(filename='log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()

    # Create ThreadPoolExecutor for API calls
    with ThreadPoolExecutor(max_workers=MAX_THREADS_API_CALL) as api_executor:
        api_futures = [api_executor.submit(process_location) for _ in range(MAX_THREADS_API_CALL)]

    # Create ThreadPoolExecutor for file writing
    with ThreadPoolExecutor(max_workers=MAX_THREADS_FILE_WRITE) as file_executor:
        file_futures = [file_executor.submit(write_to_file) for _ in range(MAX_THREADS_FILE_WRITE)]

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
