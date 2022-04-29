# Off Chain
API para mantener actualizado el balance crypto de un usuario a partir de eventos que se generan fuera de la blockchain.

## Desarrollado en:

* [Python 3.8](https://www.python.org/)
* [Django 3.2.12](https://www.djangoproject.com/)
* [Django Rest Framework 3.13.1](https://www.django-rest-framework.org/)

## Deploy

### [Docker]()
```sh
$ docker-compose build
$ docker-compose up
$ docker exec -it container_id python manage.py createsuperuser
```

Bajar el servicio
```sh
$ docker-compose down
```

Para ver la documentacion de la api puede utilizar [docs](http://0.0.0.0:8000/api/v1/docs)

### [Virtualenv](https://virtualenv.pypa.io/en/latest/index.html)

```sh
$ pip install virtualenv
$ virtualenv off_chain
$ source off_chain/bin/activate
$ pip install -r requirements_development.txt
$ python manage.py makemigrations --settings=off_chain.settings.development
$ python manage.py migrate --settings=off_chain.settings.development
$ python manage.py createsuperuser --settings=off_chain.settings.development
$ python manage.py runserver localhost:8080 --settings=off_chain.settings.development
```
Para ver la documentacion de la api puede utilizar [docs](http://localhost:8080/api/v1/docs)


## Test

* [pytest](https://docs.pytest.org/en/7.1.x/)
  ```sh
  $ pytest
  ```
se puede ver el reporte coverage en /htmlcov

* [tox](https://tox.wiki/en/latest/)
  ```sh
  $ tox
  ```
