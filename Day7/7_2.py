"""
Create a json file in following format.    { 
""folder_name_1"": [filename_1, filename_2, ....], 
""folder_name_2"": [filename_1, filename_2, .... 
        . 
        . 
        . 

    } 
Fetch folder names from the json file and if that folder is present in
a predefined location using pythonic way then check if all the files mentioned in the
list is present or not. 
"""
import os
import json

def check_files_in_folders(json_file, predefined_location):
    with open(json_file, 'r') as file:
        data = json.load(file)

    for folder_name, files_list in data.items():
        folder_path = os.path.join(predefined_location, folder_name)

        if not os.path.exists(folder_path):
            print(f"Folder '{folder_name}' not found in the predefined location.")
            continue

        print(f"Checking files in folder: {folder_name}")
        for filename in files_list:
            file_path = os.path.join(folder_path, filename)
            if os.path.exists(file_path):
                print(f"File '{filename}' is present in folder '{folder_name}'.")
            else:
                print(f"File '{filename}' is NOT present in folder '{folder_name}'.")

if __name__ == "__main__":
    json_file = "data.json"
    predefined_location = "/home/techno-510/Desktop/Python-Training/Day7"
    check_files_in_folders(json_file, predefined_location)
