"""
Write a python program to convert XML string to dictionary. (Regex) 

        ========================== 

        Input: 

                <abc>123</abc>       

                <pqr>456</pqr> 

                <xyz>789</xyz> 

        Output: 

        { 

                "abc":"123", 

                "pqr":"456", 

                "xyz":"789" 

        } 
"""


import re


def xml_to_dict(xml_string):
    pattern = r"<(\w+)>(.*?)</\1>"
    matches = re.findall(pattern, xml_string)
    return dict(matches)


# Example usage
xml_string = """
<abc>123</abc>
<pqr>456</pqr>
<xyz>789</xyz>
"""

result = xml_to_dict(xml_string)
print(result)
