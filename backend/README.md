# BACKEND Rest API FastAPI

- Al clonar el repositorio hacer los siguientes pasos (se ejecutara en el puerto 8000, asegurece de que no tiene otras aplicaciones corriendo en ese puerto):
  cd backend
  pip install -r requirements.txt
  cd app
  uvicorn app:app --reload

Documentation

- porfavor ir a la ruta localhost:8000/docs

EndPoints:
Flota:
GET /api/service_cost -> Retorna un objeto con toda la lista con ingresos.
GET /api/service_topten -> Retorna un objeto con una lista con los 10 servicios más costosos.
GET /api/service_count-> Retorna un objeto con una lista con la cantidad de servicios por mes
GET /api/mantenciones ->Retorna un objeto con una lista con las mantenciones
GET /api/taxis -> Retorna un objeto con una lista con los taxis
GET /api/servicios -> Retorna un objeto con una lista con los servicios

            Consideraciones backend:
                consideraciones backend faltan algunas validaciones de tipo middleware.
                el proyecto no usara variables de entorno
                faltan revisar el coverage aun falta...
                test unitarios basicos.

            Consideraciones front-end:
                se agrego un poco de logica en el frontend que no se agrego en el backend
                el proyecto no usara variables de entorno

Test con pytest y coverage
Luego de correr la aplicacion con 'uvicorn app:app --reload' abrir otra terminal y ejecutar el comando 'pytest' y coverage.
