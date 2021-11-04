from OSMPythonTools.nominatim import Nominatim
from bs4 import BeautifulSoup
import requests
import ssl

from flask import Flask, request

app = Flask(__name__)

ssl._create_default_https_context = ssl._create_unverified_context

# OpenStreetMaps: Address -> Address enhanced
def queryOSM(string):
    nominatim = Nominatim()
    output = nominatim.query(string)
    return output.toJSON()[0]


# BeautifulSoup: Address -> Entity
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

# "ENDPOINT"
@app.route("/getEntity")
def query_example():
    output = getEntity(request.args.get("address"))
    return f"OSM OUTPUT: {output[0]} <br> BS4 OUTPUT: {output[1]}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)

# python 04_Azure_Docker_Flask.py
# http://127.0.0.1:80/getEntity?address=Warschauer%20Stra%C3%9Fe%2076

# ACR/ACI
# http://run-python-flask-api-in-docker.westeurope.azurecontainer.io/getEntity?address=Warschauer%20Stra%C3%9Fe%2076

# RSC
# 
