
# json to string: str = json.dumbs(js)
# string to json: js = json.loads(str)
# you can also access/change json parameters by index them directly from object js:
#      example. print js['city'] or print json.loads(str)['temperature']

import json
from flask import Flask, request, Response
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

# GET requests use params to specify which resource is gonna be read
# try GET localhost:3000/app/v2/930djf43jkdf02
@app.route('/app/<paramVersion>/<paramId>', methods = ['GET'])
def get_task_by_params(paramVersion, paramId):

    obj = json.loads('{}')
    obj['version'] = paramVersion
    obj['id'] = paramId
    str = json.dumps(obj)

    return Response(str, status = 200, mimetype = 'application/json')

# GET requests use queries to input settings to read a register
# try GET localhost:3000/app/?city=Seattle&data=temperature
@app.route('/app/', methods = ['GET'])
def get_task_by_query():

    obj = json.loads('{}')
    obj['city'] = request.args.get('city')
    obj['data'] = request.args.get('data')
    str = json.dumps(obj)

    return Response(str, status = 200, mimetype = 'application/json')

# POST requests use its body's content to create a new register
# try POST localhost:3000/app (don't forget to send a json as body content)
@app.route('/app/', methods = ['POST'])
def post_task():

    obj = json.loads('{}')
    obj['version'] =  request.json['version']
    obj['id'] =  request.json['id']
    str = json.dumps(obj)

    return Response(str, status = 200, mimetype = 'application/json')

# PUT requests use its body's content to update an existing register
# try PUT localhost:3000/app (don't forget to send a json as body content)
@app.route('/app/', methods = ['PUT'])
def put_task():

    obj = json.loads('{}')
    obj['version'] =  request.json['version']
    obj['id'] =  request.json['id']
    str = json.dumps(obj)

    return Response(str, status = 200, mimetype = 'application/json')

# DELETE requests use its params to specify which element should be deleted
# try DELETE localhost:3000/app/1
@app.route('/app/<paramId>', methods = ['DELETE'])
def delete_task(paramId):

    obj = json.loads('{}')
    obj['id'] =  paramId
    str = json.dumps(obj)

    return Response(str, status = 200, mimetype = 'application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
