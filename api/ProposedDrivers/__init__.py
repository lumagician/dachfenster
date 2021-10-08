import logging

import os
import azure.functions as func
import json
from azure.data.tables import TableClient
from azure.core.exceptions import HttpResponseError


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    access_key = os.getenv("TABLES_PRIMARY_STORAGE_ACCOUNT_KEY")
    endpoint_suffix = os.getenv("TABLES_STORAGE_ENDPOINT_SUFFIX")
    account_name = os.getenv("TABLES_STORAGE_ACCOUNT_NAME")
    endpoint = "{}.table.{}".format(account_name, endpoint_suffix)
    connection_string = "DefaultEndpointsProtocol=https;AccountName={};AccountKey={};EndpointSuffix={}".format(
    account_name, access_key, endpoint_suffix)
    table_name = "Route"

    with TableClient.from_connection_string(connection_string, table_name) as table_client:
        try:
            parameters = {u"hascar": True }
            driver_filter = u"HasCar eq @hascar"
            queried_entities = table_client.query_entities(
                query_filter=driver_filter, select=[
                    "RowKey",
                    "StartAddressZipCode",
                "StartAddressCity",
                "DestinationAddressZipCode",
                "DestinationAddressCity"],
                parameters = parameters
            )

            items = []
            for entity_chosen in queried_entities:
                item = {
                    'title': entity_chosen['RowKey']
                }
                items.append(item)
            
            return func.HttpResponse(json.dumps(items), mimetype = 'application/json')
        except HttpResponseError as e:
            logging.error(e)
            return func.HttpResponse(json.dumps([]), mimetype = 'application/json')


