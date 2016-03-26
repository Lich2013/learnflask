from learnflask import app

@app.route('/')
def index():
    list = []
    for x in app.config:
        list.append((x, app.config[x]))
    return 'hello, world'+str(list)