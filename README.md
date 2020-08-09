# Example Flask module microservice

Using Flask to build a Restful API Server.

Integration with bellow extensions.

### Extension:
- Restful: [Flask-restplus](http://flask-restplus.readthedocs.io/en/stable/)

- SQL ORM: [Flask-SQLalchemy](http://flask-sqlalchemy.pocoo.org/2.1/)

- Testing: [Flask-Testing](http://flask.pocoo.org/docs/0.12/testing/)

## Installation

Install with pip:

```
$ pip install -r requirements.txt
```

## Flask Application Structure 
```
.
├── Dockerfile
├── OWNERS
├── README.md
├── SOURCE.md
├── __init__.py
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── generic.py
│   │   └── webservices
│   │       ├── __init__.py
│   │       ├── documentation.py
│   │       ├── forms.py
│   │       ├── sso_integrations.py
│   │       ├── validations.py
│   │       └── webservice_crud.py
│   ├── forms.py
│   ├── models.py
│   ├── signals.py
│   ├── templates
│   │   ├── index.template.html
│   │   └── voen_list.html
│   └── utils
│       ├── __init__.py
│       ├── apidoc.py
│       ├── exceptions.py
│       ├── logger.py
│       ├── login_decor.py
│       ├── parser.py
│       ├── response.py
│       ├── sagabase.py
│       └── urlparser.py
├── docker-compose.yml
├── docs
│   ├── app
│   │   ├── api
│   │   │   ├── generic.html
│   │   │   ├── index.html
│   │   │   └── webservices
│   │   │       ├── documentation.html
│   │   │       ├── forms.html
│   │   │       ├── index.html
│   │   │       ├── sso_integrations.html
│   │   │       ├── validations.html
│   │   │       └── webservice_crud.html
│   │   ├── forms.html
│   │   ├── index.html
│   │   ├── models.html
│   │   ├── signals.html
│   │   └── utils
│   │       ├── apidoc.html
│   │       ├── exceptions.html
│   │       ├── index.html
│   │       ├── logger.html
│   │       ├── login_decor.html
│   │       ├── parser.html
│   │       ├── response.html
│   │       ├── sagabase.html
│   │       └── urlparser.html
│   ├── instance
│   │   ├── config.html
│   │   └── index.html
│   └── run.html
├── instance
│   ├── __init__.py
│   └── config.py
├── make_doc.sh
├── requirements.txt
├── run.py
└── tests
    ├── runner.py
    ├── test_authorization.py
    ├── test_permission.py
    ├── test_response.py
    ├── test_service_list_api.py
    ├── test_structure.py
    ├── test_system.py
    ├── test_webservice.py
    └── utilities.py

13 directories, 67 files
```


## Flask Configuration

#### Example

```
app = Flask(__name__)
app.config['DEBUG'] = True
```
### Configuring From Files

#### Example Usage

```
app = Flask(__name__ )
app.config.from_pyfile('config.Development.cfg')
```

#### cfg example

```

##Flask settings
DEBUG = True  # True/False
TESTING = False

##SWAGGER settings
SWAGGER_DOC_URL = '/api'

....


```

#### Builtin Configuration Values

SERVER_NAME: the name and port number of the server. 

JSON_SORT_KEYS : By default Flask will serialize JSON objects in a way that the keys are ordered.

- [reference¶](http://flask.pocoo.org/docs/0.12/config/)


 
## Run Flask
### Run flask for develop
```
$ python run.py
```
In flask, Default port is `5000`

### Run flask for production

** Run with gunicorn **

```
$ gunicorn -w 4 -b 127.0.0.1:5000 run:app

```

* -w : number of worker
* -b : Socket to bind


### Run with Docker

```
$ docker build -t flask-example .

$ docker run -p 5000:5000 --name flask-example flask-example 

$ docker-compose up --build -d
 
```

In image building, the app folder will also add into the image


## Unittest
```
$ cd tests/
$ nose2
```

## Reference

Offical Website

- [Flask](http://flask.pocoo.org/)
- [Flask Extension](http://flask.pocoo.org/extensions/)
- [Flask restplus](http://flask-restplus.readthedocs.io/en/stable/)
- [Flask-SQLalchemy](http://flask-sqlalchemy.pocoo.org/2.1/)
- [gunicorn](http://gunicorn.org/)

Tutorial

- [Flask Overview](https://www.slideshare.net/maxcnunes1/flask-python-16299282)
- [In Flask we trust](http://igordavydenko.com/talks/ua-pycon-2012.pdf)

[Wiki Page](https://github.com/tsungtwu/flask-example/wiki)


## Changelog

- Version 1.0 : Beta version
