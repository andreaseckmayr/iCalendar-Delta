'''
python: 3.11
2023-03-13
A. Eckmayr
'''

import os
import sys
from flask import Flask
from flask import jsonify
from flask import request
from flask import Response
from flask import send_from_directory

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test() -> str:
    ''' api healthcheck '''
    return Response('Hello, World!', status=200)


@app.route('/calendars/{file}')
def get_calendar(file: str) -> Response:
    return send_from_directory('reports', file)
