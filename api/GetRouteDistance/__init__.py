import logging

import azure.functions as func

import json

url = "http://dev.virtualearth.net/REST/V1/Routes/Driving?o=json&wp.0=Aeugst am Albis&avoid=minimizeTolls&key=AmzCNKlINpVWMJENuTPqdfiR-B5Kg1YM95MtahgZtn-AvzMukcU9GqaZ9Wey9ADd&wp.1=Bonstetten"

x = {
    "AdressOne" : "Burgdorfstrsse 30, 3510 Konolfingen",
    "AdressTwo" : "Burgdorfstrsse 30, 3510 Konolfingen",
    "AdressThree" : "Burgdorfstrsse 30, 3510 Konolfingen",
    "AdressFour" : "Burgdorfstrsse 30, 3510 Konolfingen"
}


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    r = request.get(url)

    return func.HttpResponse(
            r.json(),
            status_code=200,
            mimetype = 'application/json'
    )
