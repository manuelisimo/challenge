# Django CRUD API challenge
by Manuel Aguilera López

## Setup

First clone the repo and set up the virtual environment

```shell
git clone git@github.com:manuelisimo/challenge.git
cd challenge
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Then run the Django migrations

```shell
 ./manage.py migrate
```

Optionally create an admin user

```shell
./manage.py createsuperuser --username manuel --email manuel@manuel.codes
```

## Retrieve external data

Loading data from the graphql api is implemented as an admin command called import:

```shell
 ./manage.py import
```

## Run the CRUD API

First start the development server

```shell
./manage.py import
```

And then the API is available under `http://127.0.0.1:8000/planets/`.   

```shell
http http://127.0.0.1:8000/planets/ | jq
```

## Run the tests

To run the tests use the django admin

```shell
./manage test
```
