import logging

import azure.functions as func
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('username')

    return func.HttpResponse(json.dumps([
        {
            'title': 'Func Result 1'
        },
        {
            'title': 'Func Result 2'
        }
    ]), mimetype = 'application/json')


