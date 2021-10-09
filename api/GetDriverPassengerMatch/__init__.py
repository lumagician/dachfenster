import logging

import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Gets a specific driver passenger match.')

    driver_name = req.params.get('driver')
    passenger_name = req.params.get('passenger')

    result = {
        'driver': driver_name,
        'passenger': passenger_name
    }

    return func.HttpResponse(
             json.dumps(result),
             mimetype='application/json',
             status_code=200
    )
