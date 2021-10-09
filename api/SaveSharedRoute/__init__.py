import logging

import azure.functions as func
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Saving shared data')

    day_preferences = req.get_json()


    return func.HttpResponse(
            json.dumps(day_preferences),
            mimetype = 'application/json',
            status_code=200
    )
