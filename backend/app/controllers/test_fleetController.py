
import unittest
from unittest.mock import patch, Mock
import pytest
import json
import jsonpath
from fleetController import suma, resta, get_service_count, get_mantenciones, get_taxis, get_servicios, get_service_cost, get_service_topten, mathGasolineCostByService, getService, getCar, getMaintenance, maintenanceByServiceId, monthCountByService, tenMostExpensiveServices
import requests

port = 8000
baseUrl = "http://localhost:{}/".format(port)


def test_suma():
    print(suma(2, 2))
    assert suma(2, 2) == 4


def test_resta():
    print(resta(2, 2))
    assert resta(2, 2) == 0


""" Testing api/service_count should return a object(dict) Json response with status 200 """


def test_get_service_count():
    path = "service_count"
    response = requests.get(url=baseUrl+path)
    responseJson = json.loads(response.text)
    #collection = read_all_articles()
    assert isinstance(responseJson, dict)
    #assert isinstance(responseJson, list)
    assert response.status_code == 200
    #assert jsonpath.jsonpath(responseJson, '$.data.type_of')[0] == 'article'
    #assert jsonpath.jsonpath(responseJson, '$.data.id')[0] == 2
    #assert isinstance(json.dumps({collection.data}), list)


""" Testing api/service_cost should return a object(dict) Json response with status 200 """


def test_get_service_cost():
    path = "service_cost"
    response = requests.get(url=baseUrl+path)
    responseJson = json.loads(response.text)
    assert isinstance(responseJson, dict)
    #assert isinstance(responseJson, list)
    assert response.status_code == 200


""" Testing api/service_topten should return a object(dict) Json response with status 200 """


def test_get_service_topten():
    path = "service_topten"
    response = requests.get(url=baseUrl+path)
    responseJson = json.loads(response.text)
    assert isinstance(responseJson, dict)
    #assert isinstance(responseJson, list)
    assert response.status_code == 200


""" Testing api/taxis should return a object(dict) Json response with status 200 """


def test_get_taxis():
    path = "taxis"
    response = requests.get(url=baseUrl+path)
    responseJson = json.loads(response.text)
    assert isinstance(responseJson, dict)
    #assert isinstance(responseJson, list)
    assert response.status_code == 200


""" Testing api/mantenciones should return a object(dict) Json response with status 200 """


def test_get_mantenciones():
    path = "mantenciones"
    response = requests.get(url=baseUrl+path)
    responseJson = json.loads(response.text)
    assert isinstance(responseJson, dict)
    #assert isinstance(responseJson, list)
    assert response.status_code == 200


""" Testing api/servicios should return a object(dict) Json response with status 200 """


def test_get_servicios():
    path = "servicios"
    response = requests.get(url=baseUrl+path)
    responseJson = json.loads(response.text)
    assert isinstance(responseJson, dict)
    #assert isinstance(responseJson, list)
    assert response.status_code == 200


""" Testing method mathGasolineCostByService should return a object(dict) Json response"""
# @staticmethod


@pytest.mark.asyncio
async def test_mathGasolineCostByService():
    responseJson = await mathGasolineCostByService(690, "05-19-2022", 35)
    assert isinstance(responseJson, dict)

""" Testing method getService should return a object(dict) Json response"""


@pytest.mark.asyncio
async def test_getService():
    responseJson = await getService(2)
    assert isinstance(responseJson, dict)

""" Testing method getCar should return a object(dict) Json response"""


@pytest.mark.asyncio
async def test_getCar():
    responseJson = await getCar(2)
    assert isinstance(responseJson, dict)

""" Testing method getMaintenance should return a object(dict) Json response"""


@pytest.mark.asyncio
async def test_getMaintenance():
    responseJson = await getMaintenance(2)
    assert isinstance(responseJson, dict)

""" Testing method maintenanceByServiceId should return a object(dict) Json response"""


@pytest.mark.asyncio
async def test_maintenanceByServiceId():
    responseJson = await maintenanceByServiceId(2)
    assert isinstance(responseJson, dict)

""" Testing method monthCountByService should return a object(dict) Json response"""


@pytest.mark.asyncio
async def test_monthCountByService():
    responseJson = await monthCountByService()
    #collection = read_all_articles()
    assert isinstance(responseJson, dict)

""" Testing method tenMostExpensiveServices should return a object(dict) Json response"""


@pytest.mark.asyncio
async def test_tenMostExpensiveServices():
    responseJson = await tenMostExpensiveServices()
    assert isinstance(responseJson, dict)


"""
def func(x):
    return x + 1


def test_answer():
    assert func(4) == 5
def test_read_all_articles():
    # print(event)
    # print(context)
    response = read_all_articles()
    print(response)
    assert response.status_code == 200
    #self.assertEqual(result, 15)

# class testCalc(unittest.TestCase):
# if __name__ == '__main__':
 # unittest.main()


 import requests
import json
import jsonpath

baseUrl = "https://reqres.in/"

def test_fetch_user() :
    path = "api/users/2"
    response = requests.get(url=baseUrl+path)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson,'$.data.first_name')[0] == 'Janet'
    assert jsonpath.jsonpath(responseJson,'$.data.id')[0] == 2


def test_create_delete_user() :
    file = open('TestData/user.json',"r")
    path = "api/users"
    inputData = json.loads(file.read())
    response = requests.post(url=baseUrl+path,json=inputData)
    responseJson = json.loads(response.text)
    assert response.status_code == 201
    assert jsonpath.jsonpath(responseJson,'$.name')[0] == inputData["name"]
    id = jsonpath.jsonpath(responseJson,'$.id')[0]
    response = requests.delete(url=baseUrl+path+'/'+id)
    assert response.status_code == 204
"""
