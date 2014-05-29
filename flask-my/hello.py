from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	index = '<h2>index page</h2>'
	return index

@app.route('/hello')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug = True)
