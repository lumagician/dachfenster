import logging

import os
import azure.functions as func
from azure.data.tables import TableClient
from azure.core.exceptions import HttpResponseError
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Requesting specific route.')

    name = req.params.get('name')

    access_key = os.getenv("TABLES_PRIMARY_STORAGE_ACCOUNT_KEY")
    endpoint_suffix = os.getenv("TABLES_STORAGE_ENDPOINT_SUFFIX")
    account_name = os.getenv("TABLES_STORAGE_ACCOUNT_NAME")
    endpoint = "{}.table.{}".format(account_name, endpoint_suffix)
    connection_string = "DefaultEndpointsProtocol=https;AccountName={};AccountKey={};EndpointSuffix={}".format(
    account_name, access_key, endpoint_suffix)
    table_name = "Route"

    with TableClient.from_connection_string(connection_string, table_name) as table_client:
        try:
            route = table_client.get_entity('testing', name)

            result = {
                'startAddress': {
                    'street': route['StartAddressStreet'],
                    'zipCode': route['StartAddressZipCode'],
                    'city': route['StartAddressCity']
                },
                'destinationAddress': {
                    'street': route['DestinationAddressStreet'],
                    'zipCode': route['DestinationAddressZipCode'],
                    'city': route['DestinationAddressCity']
                }
            }
            
            return func.HttpResponse(
                json.dumps(result),
                mimetype='application/json',
                status_code=200
            )
        except HttpResponseError as e:
            logging.error(e)
            return func.HttpResponse(json.dumps([]), mimetype = 'application/json')

