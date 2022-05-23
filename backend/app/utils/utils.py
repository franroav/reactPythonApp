import json
import os
from pathlib import Path


def get_mantenciones():
    # Opening JSON Mantenciones file
    try:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        curr_dir = (str(Path(__file__).parent)).replace('\\', '/')
        API_URL = "{}/mantenciones.json".format(curr_dir)
        # print(API_URL)
        with open(API_URL, "r") as json_file:
            data = json.load(json_file)

            return data
    except FileNotFoundError as e:
        print('ERROR: ', e)
        return {
            'error': 'ERROR',
            'statusCode': 404,
            'payload': json.dumps({
                'message': f"Error de la aplicación: {str(e)}"
            })
        }


def get_servicios():
    # Opening JSON Servicios file
    try:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        curr_dir = (str(Path(__file__).parent)).replace('\\', '/')
        API_URL = "{}/servicios.json".format(curr_dir)
        # print(API_URL)
        with open(API_URL, "r") as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError as e:
        print('ERROR: ', e)
        return {
            'error': 'ERROR',
            'statusCode': 404,
            'payload': json.dumps({
                'message': f"Error de la aplicación: {str(e)}"
            })
        }


def get_taxis():
    # Opening JSON Taxis file
    try:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        curr_dir = (str(Path(__file__).parent)).replace('\\', '/')
        API_URL = "{}/taxis.json".format(curr_dir)
        # print(API_URL)
        with open(API_URL, "r") as json_file:
            data = json.load(json_file)

            return data
    except FileNotFoundError as e:
        print('ERROR: ', e)
        return {
            'error': 'ERROR',
            'statusCode': 404,
            'payload': json.dumps({
                'message': f"Error de la aplicación: {str(e)}"
            })
        }
