from OSMPythonTools.nominatim import Nominatim
from bs4 import BeautifulSoup
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# OpenStreetMaps: Address -> Address enhanced
def queryOSM(string):
    nominatim = Nominatim()
    output = nominatim.query(string)
    return output.toJSON()[0]


# BeautifulSoup: Address -> Type of Entity
def queryBS4(string):

    params = {"q": string, "hl": "en"}
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"
    }
    url = "https://www.google.com/search"
    request = requests.get(url, params=params, headers=headers).content

    soup = BeautifulSoup(request, "html.parser")

    return soup.find_all(class_="YhemCb")[1].get_text()


# OpenStreetMaps + BeautifulSoup
def getEntity(string):
    OSM = queryOSM(string).get("display_name")
    return [OSM, queryBS4(OSM)]


#############################################################

# Example 1
output = getEntity("Warschauer Straße 76")
print(f"OSM OUTPUT: {output[0]}")
print(f"BS4 OUTPUT: {output[1]}")

# Example 2
output = getEntity("Am Hamburger bhf 4")
print(f"OSM OUTPUT: {output[0]}")
print(f"BS4 OUTPUT: {output[1]}")