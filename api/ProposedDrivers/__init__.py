import logging

import os
import azure.functions as func
import json
from azure.data.tables import TableServiceClient


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    access_key = os.getenv("TABLES_PRIMARY_STORAGE_ACCOUNT_KEY")
    endpoint_suffix = os.getenv("TABLES_STORAGE_ENDPOINT_SUFFIX")
    account_name = os.getenv("TABLES_STORAGE_ACCOUNT_NAME")
    endpoint = "{}.table.{}".format(account_name, endpoint_suffix)
    connection_string = "DefaultEndpointsProtocol=https;AccountName={};AccountKey={};EndpointSuffix={}".format(
    account_name, access_key, endpoint_suffix)
    table_name = "Route"

    with TableServiceClient.from_connection_string(conn_str=connection_string) as table_service:
        list_tables = table_service.list_tables()

        all_tables = ''
        for table in list_tables:
            all_tables += table.name


        return func.HttpResponse(json.dumps([
            {
                'title': 'Func Result 1 ' + all_tables
            },
            {
                'title': 'Func Result 2' + connection_string
            }
        ]), mimetype = 'application/json')


