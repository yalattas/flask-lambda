from flask import request
from flask_lambda import FlaskLambda

import json
from config.settings import api_version
from controller.dashboard import DashboardController
# flask app ---------------------------------
app = FlaskLambda(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY='e945f086-f02c-42dd-86bf-17720cbf9f7d',
    PREFERRED_URL_SCHEME='http'
)
app.url_map.strict_slashes = False
# flask app ---------------------------------

@app.route(f'/api/{api_version}/dashboard/', methods=['GET'])
def get_dashboard():
    body = DashboardController.get_dashboard(request.json)
    return (
        json.dumps({'message': body}),
        200,
        {'Content-Type': 'application/json'}
    )

@app.route(f'/api/{api_version}/dashboards/', methods=['GET'])
def get_dashboards():
    body = DashboardController.get_dashboards(request.json)
    return (
        json.dumps({'message': body}),
        200,
        {'Content-Type': 'application/json'}
    )

if __name__ == '__main__':
    # asgi_app = WsgiToAsgi(app)
    app.run(debug=True, threaded=True, host='0.0.0.0', port=8080)