import logging

import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    driver = req.params.get('driver')
    passenger = req.params.get('passenger')
    
    result = {
        'driver': driver,
        'passenger': passenger
    }

    return func.HttpResponse(
             json.dumps(result),
             mimetype='application/json',
             status_code=200
    )
