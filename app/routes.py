from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"

@app.route('/create', methods = ['POST'])
def create():
    return "create account here"

@app.route('/login', methods = ['POST'])
def create():
    return "login here"