from learnflask import app

@app.route('/')
def index():
    return 'hello, world', 403