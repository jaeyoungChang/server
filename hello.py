from flask import Flask, Response, jsonify, json, request, render_template, redirect
from flask_cors import CORS

import cv2

app = Flask(__name__)
cors = CORS(app, resources={
  r"/*": {"origin": "*"},
  r"/api/*": {"origin": "*"},
})

@app.route('/')
def hello_world():
    print('hello_world called')
    data = {"some_key": "some_value"}
    response = app.response_class(response=json.dumps(data),
                                  status=200,
                                  mimetype='application/json')
    return response

@app.route('/sample', methods=['POST', 'GET'])
def sample():
    if request.method == 'POST':
        f = request.files['file']
        print('file', f)

        print('cv2 version :', cv2.__version__)

        if f:
            # print(f.read())
            pass

        # img = cv2.imread(f)
        # cv2.imshow('image', img)

        data = {"some_key": "response completed"}
        response = app.response_class(response=json.dumps(data),
                                      status=200,
                                      mimetype='application/json')
        return response
    elif request.method == 'GET':
	return 'GET return'

@app.route('/redirectsrc/', methods=['GET'])
def redirect_src_sample():
    print('redirect_src_sample called')
    return redirect('/redirectdest')
    # return 'redirectsrc'

@app.route('/redirectdest/', methods=['GET'])
def redirect_dest_sample():
    print('redirect_dest_sample called')
    return 'redirect_dest_sample'


if __name__ == '__main__':
   app.run()
