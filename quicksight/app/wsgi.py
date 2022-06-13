import json
from flask_lambda import FlaskLambda

from handler.error import general_error
from config.clients import ssm

app = FlaskLambda(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY='<SAMPLE_KEY>',
    PREFERRED_URL_SCHEME='http'
)
@app.route('/test', methods=['GET'])
def test():
    # return aws_invoke(app,event,block_headers=False)
    statusCode = 200
    try:
        print('hello')
    except Exception as e:
        statusCode = 500
        general_error(e)

    data = {'message':'initial'}
    if statusCode != 200:
        data['message'] = 'execution failed. Check cloudwatch'
    else:
        data['message'] = 'function executed perfectly'

    return (
        json.dumps(data, indent=4, sort_keys=True),
        200,
        {'Content-Type': 'application/json'}
    )


if __name__ == '__main__':
    # asgi_app = WsgiToAsgi(app)
    app.run(threaded=True, host='0.0.0.0', port=8080)