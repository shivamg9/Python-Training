"""
Create a log file such as when the content of log file exceeds the 1000 line, 
the new log file should get created and the older log file should be renamed to {logfilename}0.log ,
{logfilename}1.log , {logfilename}2.log etc.
"""

import os
import json
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    file_handler = RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=9)
    file_handler.setLevel(logging.DEBUG)

    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(log_format)

    logger.addHandler(file_handler)
    return logger

def check_files_in_folders(json_file, predefined_location, log_file):
    logger = setup_logger(log_file)

    with open(json_file, 'r') as file:
        data = json.load(file)

    for folder_name, files_list in data.items():
        folder_path = os.path.join(predefined_location, folder_name)

        if not os.path.exists(folder_path):
            logger.error("Folder '%s' not found in the predefined location.", folder_name)
            continue

        logger.info("Checking files in folder: %s", folder_name)
        for filename in files_list:
            file_path = os.path.join(folder_path, filename)
            if os.path.exists(file_path):
                logger.info("File '%s' is present in folder '%s'.", filename, folder_name)
            else:
                logger.critical("File '%s' is NOT present in folder '%s'.", filename, folder_name)

if __name__ == "__main__":
    json_file = "data.json"
    predefined_location = "/home/techno-510/Desktop/Python-Training/Day7"
    log_file = "log_file.log"

    check_files_in_folders(json_file, predefined_location, log_file)