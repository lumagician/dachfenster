import logging

import os
import json
import azure.functions as func
from azure.data.tables import TableClient
from azure.core.exceptions import HttpResponseError
from furl import furl
import requests
from azure.data.tables import UpdateMode

BASE_URL = "http://dev.virtualearth.net/REST/V1/Routes/Driving"
LOCATIONS_BASE_URL = 'http://dev.virtualearth.net/REST/v1/Locations'

def get_location(street, zipCode):
    f = furl(LOCATIONS_BASE_URL)
    f.args["o"] = "json"
    f.args["key"] = os.getenv("BING_MAPS_KEY")
    f.args["countryRegion"] = "CH"
    f.args["postalCode"] = zipCode
    f.args["addressLine"] = street
    logging.info(f.url)
    r = requests.get(f.url)
    j = r.json()
    first_resource = j['resourceSets'][0]['resources'][0]
    coordinates = first_resource['point']['coordinates']
    return str(coordinates[0]) + ',' + str(coordinates[1])

def get_duration_with_passenger(driver_start, passenger_start, passenger_end, driver_end):
    f = furl(BASE_URL)
    f.args["o"] = "json"
    f.args["key"] = os.getenv("BING_MAPS_KEY")
    f.args["optimize"] = "time"
    f.args["wp.0"] = driver_start
    f.args["vwp.1"] = passenger_start
    f.args["vwp.2"] = passenger_end
    f.args["wp.3"] = driver_end
    r = requests.get(f.url)
    j = r.json()
    first_resource = j['resourceSets'][0]["resources"][0]
    result = {}
    result['travelDuration'] = first_resource["travelDuration"]
    return result

def get_duration_without_passenger(driver_start, driver_end):
    f = furl(BASE_URL)
    f.args["o"] = "json"
    f.args["key"] = os.getenv("BING_MAPS_KEY")
    f.args["optimize"] = "time"
    f.args["wp.0"] = driver_start
    f.args["wp.1"] = driver_end
    r = requests.get(f.url)
    j = r.json()
    first_resource = j['resourceSets'][0]["resources"][0]
    result = {}
    result['travelDuration'] = first_resource["travelDuration"]
    return result

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    driver_name = req.params.get('driver')
    passenger_name = req.params.get('passenger')

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

            driver_start_address = (driver['StartAddressStreet'] + ', ' + driver['StartAddressZipCode'] +
                ' ' + driver['StartAddressCity'])
            
            passenger_start_address = (passenger['StartAddressStreet'] + ', ' + passenger['StartAddressZipCode'] +
                ' ' + passenger['StartAddressCity'])
            
            passenger_destination_address = (passenger['DestinationAddressStreet'] + ', ' + passenger['DestinationAddressZipCode'] +
                ' ' + passenger['DestinationAddressCity'])

            driver_destination_address = (driver['DestinationAddressStreet'] + ', ' + driver['DestinationAddressZipCode'] +
                ' ' + driver['DestinationAddressCity'])

            
            duration_without_passenger = get_duration_without_passenger(driver_start_address, driver_destination_address)

            duration_with_passenger = get_duration_with_passenger(driver_start_address,
                passenger_start_address, passenger_destination_address, driver_destination_address)


            driver['DurationWithoutPassenger'] = duration_without_passenger['travelDuration']

            table_client.upsert_entity(mode=UpdateMode.REPLACE, entity = driver)

            logging.info(str(duration_without_passenger['travelDuration']) + ' vs ' + str(duration_with_passenger['travelDuration']))

            result = {
                'PartitionKey': 'testing',
                'RowKey': driver_name + '_' + passenger_name,
                'Driver': driver_name,
                'Passenger': passenger_name,
                'Duration': duration_with_passenger['travelDuration'],
                'DriverStartCoordinates': get_location(driver['StartAddressStreet'], driver['StartAddressZipCode']),
                'PassengerStartCoordinates':  get_location(passenger['StartAddressStreet'], passenger['StartAddressZipCode']),
                'PassengerDestinationCoordinates': get_location(passenger['DestinationAddressStreet'], passenger['DestinationAddressZipCode']),
                'DriverDestinationCoordinates': get_location(driver['DestinationAddressStreet'], driver['DestinationAddressZipCode'])
            }

            with TableClient.from_connection_string(connection_string, 'TravelDuration') as duration_client:
                duration_client.upsert_entity(mode=UpdateMode.REPLACE, entity=result)
            
            return func.HttpResponse(
                json.dumps(result),
                mimetype='application/json',
                status_code=200
            )
        except HttpResponseError as e:
            logging.error(e)
            return func.HttpResponse(json.dumps([]), mimetype = 'application/json')



