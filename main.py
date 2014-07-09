#!/usr/bin/env python3
import bottle
from mongokit import Connection

connection = Connection()


app = bottle.default_app()
bottle.debug(True)
bottle.run(app=app, host="127.0.0.1", port=8080, debug=True)
