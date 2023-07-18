import requests
import xml.etree.ElementTree as ET
import os

STATIC_URL = "https://rxnav.nlm.nih.gov"

test_rxcuis = ("11289+243670")

def make_request_url(rxcuis):
    request_url = (STATIC_URL +
                   f"/REST/interaction/list.xml?rxcuis={rxcuis}"
                   )
    return request_url

def make_http_request(request_url):
    try:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None


def write_temp_xml():
    with open("temp/results.xml", "w") as f:
        f.write(unparsed_xml)
    

def get_descriptions():

    tree = ET.parse("temp/results.xml")

    root = tree.getroot()

    descriptions = root.findall(".//description")

    for desc in descriptions:
        print(desc.text)

if __name__ == "__main__":
    request_url = make_request_url(test_rxcuis)
    unparsed_xml = make_http_request(request_url)
    write_temp_xml()
    get_descriptions()
    #os.remove("temp/results.xml")



