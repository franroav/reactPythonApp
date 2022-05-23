#FROM fastapi-rest-api-crud/uvicorn-gunicorn-fastapi:python3.7

#COPY ./ ./

FROM python:3.8

LABEL maintainer="Francisco Roa <franroav@gmail.com>"

ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD python app.py
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
