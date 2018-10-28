from server import webapp

@app.route('/')
@app.route('/index')
def index():
    return "Hello, Flask World!"
