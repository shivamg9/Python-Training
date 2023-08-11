"""
Create a log file using logger module. 
Write a function display_words() in python to read lines from a text file "story.txt" 
(take the file name from user), and display those words in INFO level log, 
for those words which are less than 4 characters needs to be logged as in CRITICAL level log.  
If user enter the wrong file name in input then raise ERROR in log file  
""" 

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

log_file = "logfile.log"
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(log_format)
console_handler.setFormatter(log_format)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

def display_words():
    file_name = input("Enter the file name: ")

    try:
        with open(file_name, 'r') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    if len(word) < 4:
                        logger.critical("CRITICAL: %s", word)
                    else:
                        logger.info(word)

    except FileNotFoundError:
        logger.error("ERROR: File not found!")

if __name__ == "__main__":
    display_words()
