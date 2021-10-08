import logging

import azure.functions as func

import json
import requests

x = {
    "AdressOne" : "Burgdorfstrsse 30, 3510 Konolfingen",
    "AdressTwo" : "Burgdorfstrsse 30, 3510 Konolfingen",
    "AdressThree" : "Burgdorfstrsse 30, 3510 Konolfingen",
    "AdressFour" : "Burgdorfstrsse 30, 3510 Konolfingen"
}


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse(
            json.dumps(x),
            status_code=200
    )
