import requests
import xml.etree.ElementTree as ET
import os

'''
TODO
Add user input of drugs, how to convert drug names to rxcui?

Implement more robust output, specify the severity of medication
interaction. Maybe make it a nice formatted document?

Long term: Make a gui/webapp of it
'''

STATIC_URL = "https://rxnav.nlm.nih.gov"

test_rxcuis = ("11289+243670")

#def get_rxcuis(drug_names[]) -> str:
#waiting on API access


def make_request_url(rxcuis) -> str:
    request_url = (STATIC_URL +
                   f"/REST/interaction/list.xml?rxcuis={rxcuis}"
                   )
    return request_url

def make_http_request(request_url) -> str:
    try:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(e)
        return None


def write_temp_xml() -> None:
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



