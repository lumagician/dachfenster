import logging

import azure.functions as func

import json
import requests

url = "http://dev.virtualearth.net/REST/V1/Routes/Driving?o=json&wp.0=Aeugst am Albis&avoid=minimizeTolls&key=AmzCNKlINpVWMJENuTPqdfiR-B5Kg1YM95MtahgZtn-AvzMukcU9GqaZ9Wey9ADd&wp.1=Bonstetten"


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    r = requests.get(url)

    j = r.json()

    return func.HttpResponse(
        f"{['resourceSets'][0]['resources'][0]['travelDistance']}",
        status_code=200,
        mimetype='application/json'
    )
