from fastapi import FastAPI, APIRouter, Depends, HTTPException
import json
import pathlib
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
from config import configuration
from controllers import fleetController
import os
from os.path import dirname, basename, isfile, join
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime
import uvicorn
from models.post import Post

if os.path.isfile('.env'):
    from dotenv import load_dotenv
    load_dotenv()

app = FastAPI(title='Api de servicio de mantenimientos de autos',
              description='Esta api esta desarrollada para En el Centro de Operaciones Option.', version='1.0')

origins = ["*"]


def configure():
    ...
    configure_api_keys()
    configure_routing()


def configure_api_keys():
    curr_dir = (str(Path(__file__).parent)).replace('\\', '/')
    sercret_keys_route = curr_dir.replace('app', 'settings.json')
    print(sercret_keys_route)
    try:
        with open(sercret_keys_route, "r") as json_file:
            secret = json.load(json_file)
            file = pathlib.Path(sercret_keys_route)
            # setting my apikey secret file
            cnf = configuration
            cnf.config(secret)
            # print(cnf.keys)  # get my keys GLOBALY
            if not file.exists():
                print(
                    f"WARNING: {file} file not found, you cannot continue, please see settings_template.json")
                raise Exception(
                    "settings.json file not found, you cannot continue, please see settings_template.json")
    except FileNotFoundError as e:
        print('ERROR: ', e)
        return {
            'error': 'ERROR',
            'statusCode': 404,
            'payload': json.dumps({
                'message': f"Error de la aplicación: {str(e)}"
            })
        }


def configure_routing():
    """include static file"""
    #app.mount('/static', StaticFiles(directory='static'), name='static')
    """set CORS """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(fleetController.router, tags=['posts'])
    """ add aditional route controller like"""
    #app.include_router(fleetController.router, prefix="/users", tags=['posts'])


"""About __name__ == "__main__"¶
The main purpose of the __name__ == "__main__" is to have some code that is executed when your file is called with:
but is not called when another file imports it, like in:
PERO -> from myapp import app"""
if __name__ == '__main__':
    configure()
    # uvicorn was updated, and it's type definitions don't match FastAPI,
    # but the server and code still work fine. So ignore PyCharm's warning:
    # noinspection PyTypeChecker
    uvicorn.run(app, port=8000, host='127.0.0.1')
else:
    configure()
