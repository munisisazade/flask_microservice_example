"""
    Code documentation for Microservice
.. include:: ./README.md
"""
from main import app

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])
