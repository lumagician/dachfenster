import logging

import os
import json
import azure.functions as func
from azure.data.tables import TableClient
from azure.core.exceptions import HttpResponseError


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    driver_name = req.params.get('driver')
    passenger_name = req.params.get('passenger')
    
    result = {
        'driver': driver_name,
        'passenger': passenger_name
    }

    access_key = os.getenv("TABLES_PRIMARY_STORAGE_ACCOUNT_KEY")
    endpoint_suffix = os.getenv("TABLES_STORAGE_ENDPOINT_SUFFIX")
    account_name = os.getenv("TABLES_STORAGE_ACCOUNT_NAME")
    bing_maps_key = os.getenv("BING_MAPS_KEY")
    endpoint = "{}.table.{}".format(account_name, endpoint_suffix)
    connection_string = "DefaultEndpointsProtocol=https;AccountName={};AccountKey={};EndpointSuffix={}".format(
    account_name, access_key, endpoint_suffix)
    table_name = "Route"

    with TableClient.from_connection_string(connection_string, table_name) as table_client:
        try:
            driver = table_client.get_entity('testing', driver_name)
            passenger = table_client.get_entity('testing', passenger_name)

            logging.info(json.dumps(driver))
            logging.info(json.dumps(passenger))
            logging.info(bing_maps_key)
            
            return func.HttpResponse(
                json.dumps(result),
                mimetype='application/json',
                status_code=200
            )
        except HttpResponseError as e:
            logging.error(e)
            return func.HttpResponse(json.dumps([]), mimetype = 'application/json')



