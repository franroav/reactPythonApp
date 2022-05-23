from fastapi import APIRouter, FastAPI, HTTPException, Query
from numpy import number
from pydantic import BaseModel
from typing import Optional, Text
from services import fleetService
import json
from datetime import datetime, date
from uuid import uuid4 as uuid
import logging  # logging
import uvicorn
#from .. app import *
from models.post import Post
import requests

router = APIRouter()
srv = fleetService
posts = []

logging.basicConfig(filename='example.log', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    encoding='utf-8', level=logging.INFO)

# example testing


def suma(x, y):
    """ Add Function """
    return x + y

# example testing


def resta(x, y):
    """ Add Function """
    return x - y


""" aditional controller methods """


async def mathGasolineCostByService(cost: number, date: date, quantity: number):
    # print(cost)
    # print(quantity)
    # print(date)
    return {"cost": cost * quantity, "date": date}


async def servMaintenance(id: number):
    data_mantenciones = await srv.get_ctr_mantenciones()
    mantenciones = data_mantenciones["data"]
    filterMaintenanceByServiceId = tuple(
        filter(lambda x: x["id_servicio"] == id, mantenciones["payload"]))
    return filterMaintenanceByServiceId


async def maintenanceByServiceId(id: number):
    # find service
    service = await getService(id)
    # get maintenance list with service id
    man_serv = await servMaintenance(id)
    cost_collection = []
    for index, mantencion in enumerate(man_serv):

        car = await getCar(int(mantencion["id_auto"]))
        # get cost gasoline
        gasolineCost = await mathGasolineCostByService(int(service["unit_cost"]), mantencion["fecha_servicio"], int(car["gasoline_tank"]))
        # filter by actual and lastMonth
        cost_collection.append(gasolineCost)

    actualMonth = str(date.today()).split("-")[1]
    lastMonth = "0{}".format(str(int(str(date.today()).split("-")[1]) - 1))

    filterActualByMonth = tuple(
        filter(lambda x: str(x["date"]).split("-")[0] == actualMonth, cost_collection))
    filterLastByMonth = tuple(
        filter(lambda x: str(x["date"]).split("-")[0] == lastMonth, cost_collection))
    totalCostActualMonth = sum(c["cost"] for c in filterActualByMonth)
    totalCostLastMonth = sum(c["cost"] for c in filterLastByMonth)
    # print(actualMonth)
    response = {"service_name": service["service_name"], "total_maintenance_cost": totalCostActualMonth, "total_maintenance_cost_previous_month": totalCostLastMonth, "actual_month": str(date.today()).split(
        "-")[1], "year": str(date.today()).split("-")[0], "request_date": str(date.today()), "response_date": str(date.today())}
    # returns JSON object as
    # a dictionary
    return response


async def countServiceByMonth(id: number):
    # find service
    service = await getService(id)
    man_serv = await servMaintenance(id)
    cost_collection = []
    for index, mantencion in enumerate(man_serv):

        car = await getCar(int(mantencion["id_auto"]))
        # get cost gasoline
        gasolineCost = await mathGasolineCostByService(int(service["unit_cost"]), mantencion["fecha_servicio"], int(car["gasoline_tank"]))
        # filter by actual and lastMonth
        cost_collection.append(gasolineCost)

    actualMonth = str(date.today()).split("-")[1]
    lastMonth = "0{}".format(str(int(str(date.today()).split("-")[1]) - 1))
    filterActualByMonth = len(tuple(
        filter(lambda x: str(x["date"]).split("-")[0] == actualMonth, cost_collection)))
    filterLastByMonth = len(tuple(
        filter(lambda x: str(x["date"]).split("-")[0] == lastMonth, cost_collection)))
    response = {"service_name": service["service_name"], "total_count": filterActualByMonth, "total_count_previous_month": filterLastByMonth, "actual_month": str(date.today()).split(
        "-")[1], "year": str(date.today()).split("-")[0], "request_date": str(date.today()), "response_date": str(date.today())}
    # returns JSON object as
    # a dictionary
    return response


async def getCar(id: number):
    data_taxis = await srv.get_ctr_taxis()
    car = data_taxis["data"]
    _car = [x for x in car["payload"] if x["id"] == id]
    return _car[0]


async def getService(id: number):
    data_service = await srv.get_ctr_servicios()
    service = data_service["data"]
    _service = [x for x in service["payload"] if x["id"] == id]
    return _service[0]


async def getMaintenance(id: number):
    data_mantencion = await srv.get_ctr_mantenciones()
    mantencion = data_mantencion["data"]
    _mantencion = [x for x in mantencion["payload"] if x["id"] == id]
    return _mantencion[0]

# template


async def fleetData():
    data_mantenciones = await srv.get_ctr_mantenciones()
    data_services = await srv.get_ctr_servicios()
    data_taxis = await srv.get_ctr_taxis()
    taxis = data_taxis["data"]
    services = data_services["data"]
    mantenciones = data_mantenciones["data"]
    fleet = []
    for index, service in enumerate(services["payload"]):
        raw = {}
        man_serv = [x for x in mantenciones["payload"]
                    if x["id_servicio"] == service["id"]]
        raw["service_name"] = service["service_name"]
        raw["unit_cost"] = service["unit_cost"]
        raw["category_service"] = service["category_service"]
        raw["mantenciones"] = man_serv

        cars_collection = []
        for index, mantencion in enumerate(man_serv):
            cars = {}
            man_tax = [x for x in taxis["payload"]
                       if x["id"] == mantencion["id_auto"]]

            cars["id_auto"] = mantencion["id_auto"]
            cars["id_servicio"] = mantencion["id_servicio"]
            cars["fecha_servicio"] = mantencion["fecha_servicio"]
            cars["autos"] = man_tax
            cars_collection.append(cars)
        raw["taxis"] = cars_collection
        fleet.append(raw)

    # returns JSON object as
    # a dictionary
    return fleet


"""main controller methods """
# main function to route service_topten


async def tenMostExpensiveServices():
    """10 servicios más costosos: debe mostrar los servicios más costosos."""
    # Call to service
    data_services = await srv.get_ctr_servicios()
    services = data_services["data"]
    data = []
    # loop into service
    for index, service in enumerate(services["payload"]):
        # call to maintenance
        maintenceData = await maintenanceByServiceId(service["id"])
        data.append(maintenceData)

    # sort by cost
    response = sorted(data, key=lambda d: d["total_maintenance_cost"])
    res = response[::-1]
    x = slice(10)
    # returns JSON object as
    # a dictionary
    return {
        'statusCode': 200,
        'data': {
            'title': "top ten services",
            "statusCode": 200,
            "payload":  res[x]
        }
    }
# main function to route service_count


async def monthCountByService():
    """Cantidad de servicios por mes: debe contar cuantos servicios se han ingresado en el último mes."""
    # Call to service
    data_services = await srv.get_ctr_servicios()
    services = data_services["data"]
    data = []
    # loop into service
    for index, service in enumerate(services["payload"]):
        # call to maintenance
        maintenceData = await countServiceByMonth(service["id"])
        data.append(maintenceData)
    # returns JSON object as
    # a dictionary
    return {
        'statusCode': 200,
        'data': {
            'title': "service on demand",
            "statusCode": 200,
            "payload": data
        }
    }

# main function to route service_topten


async def monthIncomeByService():
    """Ingreso mensual: debe sumar total de costos asociado a cada mantención y agrupado por servicio(category_service)."""
    # Call to service
    data_services = await srv.get_ctr_servicios()
    services = data_services["data"]
    data = []
    # loop into service
    for index, service in enumerate(services["payload"]):
        # call to maintenance
        maintenceData = await maintenanceByServiceId(service["id"])
        data.append(maintenceData)
    # returns JSON object as
    # a dictionary
    return {
        'statusCode': 200,
        'data': {
            'title': "monthly income",
            "statusCode": 200,
            "payload": data
        }
    }


"""API SERVICE"""


@router.get('/')
def read_root():
    return {"welcome": "Welcome to my API"}


@router.get('/api/service_topten')
async def get_service_topten():
    """10 servicios más costosos: debe mostrar los servicios más costosos."""
    init_lambda = datetime.now()
    # print init funtion console log
    # print('start service_topten: {}:{}:{}:{} \n'.format(init_lambda.hour,
    # init_lambda.minute, init_lambda.second, init_lambda.microsecond))
    data = await tenMostExpensiveServices()
    logging.info(data)
    # returns JSON object as
    # a dictionary
    return data


@router.get('/api/service_count')
async def get_service_count():
    """Cantidad de servicios por mes: debe contar cuantos servicios se han ingresado en el último mes."""
    # init_lambda = datetime.now()
    # print('start service_count: {}:{}:{}:{} \n'.format(init_lambda.hour,
    # init_lambda.minute, init_lambda.second, init_lambda.microsecond))
    data = await monthCountByService()
    logging.info(data)
    # returns JSON object as
    # a dictionary
    return data


@router.get('/api/service_cost')
async def get_service_cost():
    """Ingreso mensual: debe sumar total de costos asociado a cada mantención y agrupado por servicio(category_service)."""
    #init_lambda = datetime.now()
    # print('start service_cost: {}:{}:{}:{} \n'.format(init_lambda.hour,
    # init_lambda.minute, init_lambda.second, init_lambda.microsecond))
    data = await monthIncomeByService()
    logging.info(data)
    # returns JSON object as
    # a dictionary
    return data


@router.get('/api/posts')
async def get_posts():
    # Opening JSON file
    fleet = await fleetData()
    # returns JSON object as
    # a dictionary
    return fleet


@router.get('/api/mantenciones')
async def get_mantenciones():
    # Opening JSON file
    data = await srv.get_ctr_mantenciones()
    # returns JSON object as
    # a dictionary
    return data


@router.get('/api/taxis')
async def get_taxis():
    # Opening JSON file
    data = await srv.get_ctr_taxis()
    # weather = await service.get_report_async()
    # returns JSON object as
    # a dictionary
    return data


@router.get('/api/servicios')
async def get_servicios():
    # Opening JSON file
    data = await srv.get_ctr_servicios()
    # weather = await service.get_report_async()
    # returns JSON object as
    # a dictionary
    return data
