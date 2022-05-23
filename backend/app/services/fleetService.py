import json
from requests.exceptions import Timeout, TooManyRedirects, RequestException, HTTPError, ConnectionError
from requests import get, post, put, delete, session
from typing import Optional
import httpx
import logging  # logging
from datetime import datetime, date
from utils import utils
api_key: Optional[str] = None

logging.basicConfig(filename='example.log', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    encoding='utf-8', level=logging.WARNING)


def generator_headers():

    return {
        "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
        "Access-Control-Allow-Methods": "OPTIONS,GET,POST,PUT,DELETE",
        "Access-Control-Allow-Origin": "*",
        "Content-Type": "application/json",
    }


async def get_ctr_mantenciones() -> dict:
    try:
        """ Get all mantenciones from service method """
        # log
        init_service = datetime.now()
        # print log
        # print('inicio get_ctr_mantenciones service_handler: {}:{}:{}:{} \n'.format(init_service.hour,
        # init_service.minute, init_service.second, init_service.microsecond))
        #API_URL = "https://dev.to/api"
        # ARTICLE_URL = "{}/articles".format(API_URL) # service url example
        async with httpx.AsyncClient() as client:
            # resp = await client.get(ARTICLE_URL) # service
            resp = utils.get_mantenciones()
            # resp.raise_for_status() # raise exeption

        data = resp  # resp.json()

        return {
            'statusCode': 200,
            'data': data
        }
    except HTTPError as httpErrorExeption:
        # error by connection not 200 status from api
        print(httpErrorExeption)
        logging.warning(httpErrorExeption)
        response_data = resp.raise_for_status()
        return {
            'statusCode': int(response_data['status']),
            'data': json.dumps({
                'statusCode': int(response_data['status']),
                'message': f"Error de la aplicación: {str(httpErrorExeption)}"
            })
        }
    except ConnectionError as connectionErrorExeption:
        # error by connection not status from api
        print(connectionErrorExeption)
        logging.warning(connectionErrorExeption)
        return {
            'statusCode': 500,
            'data': json.dumps({
                'statusCode': 500,
                'message': f"Error de la aplicación: {str(connectionErrorExeption)}"
            })
        }
    except Timeout as timeoutExeption:
        # Maybe set up for a retry, or continue in a retry loop
       # response_data = response.json()
        print(timeoutExeption)
        logging.warning(timeoutExeption)
        return {
            'statusCode': 408,
            'data': json.dumps({
                'statusCode': 408,
                'message': f"Error de la aplicación: {str(timeoutExeption)}"
            })
        }
    except TooManyRedirects as tooManyRedirectsExeption:
        # Tell the user their URL was bad and try a different one
        print(tooManyRedirectsExeption)
        logging.warning(tooManyRedirectsExeption)
        return {
            'statusCode': 500,
            'data': json.dumps({
                'statusCode': 500,
                'message': f"Error de la aplicación: {str(tooManyRedirectsExeption)}"
            })
        }
    except RequestException as requestExceptionExeption:
        # catastrophic error. bail. this is going to catch any error that you might find including the connection error
        print(requestExceptionExeption)
        logging.warning(requestExceptionExeption)
        return {
            'statusCode': 500,
            'data': json.dumps({
                'statusCode': 500,
                'message': f"Error de la aplicación: {str(requestExceptionExeption)}"
            })
        }
        # raise SystemExit(e)
    except Exception as e:
        print(e)
        logging.warning(e)
        return {
            'statusCode': 500,
            'data': json.dumps({
                'statusCode': 500,
                'message': f"Error de la aplicación: {str(e)}"
            })
        }


async def get_ctr_servicios() -> dict:
    try:
        """ Get all servicios from float service method """
        # log
        init_service = datetime.now()
        # print log
        # print('inicio get_ctr_servicios service_handler: {}:{}:{}:{} \n'.format(init_service.hour,
        # init_service.minute, init_service.second, init_service.microsecond))
        #API_URL = "https://dev.to/api"
        # ARTICLE_URL = "{}/articles".format(API_URL) # service url example
        async with httpx.AsyncClient() as client:
            # resp = await client.get(ARTICLE_URL) # service
            resp = utils.get_servicios()
            # resp.raise_for_status() # raise exeption

        data = resp  # resp.json()

        return {
            'statusCode': 200,
            'data': data
        }
    except HTTPError as httpErrorExeption:
        # error by connection not 200 status from api
        print(httpErrorExeption)
        logging.warning(httpErrorExeption)
        response_data = resp.raise_for_status()
        return {
            'statusCode': int(response_data['status']),
            'data': json.dumps({
                'statusCode': int(response_data['status']),
                'message': f"Error de la aplicación: {str(httpErrorExeption)}"
            })
        }
    except ConnectionError as connectionErrorExeption:
        # error by connection not status from api
        print(connectionErrorExeption)
        logging.warning(connectionErrorExeption)
        return {
            'statusCode': 500,
            'data': json.dumps({
                'statusCode': 500,
                'message': f"Error de la aplicación: {str(connectionErrorExeption)}"
            })
        }
    except Timeout as timeoutExeption:
        # Maybe set up for a retry, or continue in a retry loop
       # response_data = response.json()
        print(timeoutExeption)
        logging.warning(timeoutExeption)
        return {
            'statusCode': 408,
            'data': json.dumps({
                'statusCode': 408,
                'message': f"Error de la aplicación: {str(timeoutExeption)}"
            })
        }
    except TooManyRedirects as tooManyRedirectsExeption:
        # Tell the user their URL was bad and try a different one
        print(tooManyRedirectsExeption)
        logging.warning(tooManyRedirectsExeption)
        return {
            'statusCode': 500,
            'data': json.dumps({
                'statusCode': 500,
                'message': f"Error de la aplicación: {str(tooManyRedirectsExeption)}"
            })
        }
    except RequestException as requestExceptionExeption:
        # catastrophic error. bail. this is going to catch any error that you might find including the connection error
        print(requestExceptionExeption)
        logging.warning(requestExceptionExeption)
        return {
            'statusCode': 500,
            'data': json.dumps({
                'statusCode': 500,
                'message': f"Error de la aplicación: {str(requestExceptionExeption)}"
            })
        }
        # raise SystemExit(e)
    except Exception as e:
        print(e)
        logging.warning(e)
        return {
            'statusCode': 500,
            'data': json.dumps({
                'statusCode': 500,
                'message': f"Error de la aplicación: {str(e)}"
            })
        }


async def get_ctr_taxis() -> dict:
    try:
        """ Get all servicios from float service method """
        # log
        init_service = datetime.now()
        # print log
        # print('inicio get_ctr_taxis service_handler: {}:{}:{}:{} \n'.format(init_service.hour,
        # init_service.minute, init_service.second, init_service.microsecond))
        #API_URL = "https://dev.to/api"
        # ARTICLE_URL = "{}/articles".format(API_URL) # service url example
        async with httpx.AsyncClient() as client:
            # resp = await client.get(ARTICLE_URL) # service
            resp = utils.get_taxis()
            # resp.raise_for_status() # raise exeption

        data = resp  # resp.json()

        return {
            'statusCode': 200,
            'data': data
        }
    except HTTPError as httpErrorExeption:
        # error by connection not 200 status from api
        print(httpErrorExeption)
        logging.warning(httpErrorExeption)
        response_data = resp.raise_for_status()
        return {
            'statusCode': int(response_data['status']),
            'data': json.dumps({
                'statusCode': int(response_data['status']),
                'message': f"Error de la aplicación: {str(httpErrorExeption)}"
            })
        }
    except ConnectionError as connectionErrorExeption:
        # error by connection not status from api
        print(connectionErrorExeption)
        logging.warning(connectionErrorExeption)
        return {
            'statusCode': 500,
            'data': json.dumps({
                'statusCode': 500,
                'message': f"Error de la aplicación: {str(connectionErrorExeption)}"
            })
        }
    except Timeout as timeoutExeption:
        # Maybe set up for a retry, or continue in a retry loop
       # response_data = response.json()
        print(timeoutExeption)
        logging.warning(timeoutExeption)
        return {
            'statusCode': 408,
            'data': json.dumps({
                'statusCode': 408,
                'message': f"Error de la aplicación: {str(timeoutExeption)}"
            })
        }
    except TooManyRedirects as tooManyRedirectsExeption:
        # Tell the user their URL was bad and try a different one
        print(tooManyRedirectsExeption)
        logging.warning(tooManyRedirectsExeption)
        return {
            'statusCode': 500,
            'data': json.dumps({
                'statusCode': 500,
                'message': f"Error de la aplicación: {str(tooManyRedirectsExeption)}"
            })
        }
    except RequestException as requestExceptionExeption:
        # catastrophic error. bail. this is going to catch any error that you might find including the connection error
        print(requestExceptionExeption)
        logging.warning(requestExceptionExeption)
        return {
            'statusCode': 500,
            'data': json.dumps({
                'statusCode': 500,
                'message': f"Error de la aplicación: {str(requestExceptionExeption)}"
            })
        }
        # raise SystemExit(e)
    except Exception as e:
        print(e)
        logging.warning(e)
        return {
            'statusCode': 500,
            'data': json.dumps({
                'statusCode': 500,
                'message': f"Error de la aplicación: {str(e)}"
            })
        }
