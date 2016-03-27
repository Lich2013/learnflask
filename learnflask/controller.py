from learnflask import app
from flask import request

@app.route('/', methods=['GET'])
def index():
    list = []
    for x in app.config:
        list.append((x, app.config[x]))
    return 'hello, world'+str(list)

@app.route('/post/', methods=['POST'])
def post():
    return str(request.form)
    # return 'this is post method'
