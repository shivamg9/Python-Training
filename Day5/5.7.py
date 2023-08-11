"""
Write a python program to find Urls from a given string.(Regex) 

"""

import re


def find_urls(string):
    regex = r"https?://(?:[-\w.]|%[\da-fA-F]{2})+"
    urls = re.findall(regex, string)
    return urls


string = "Visit Google at https://www.google.com"
urls = find_urls(string)
print("URLs found:")
for url in urls:
    print(url)
