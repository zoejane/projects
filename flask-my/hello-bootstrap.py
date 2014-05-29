from flask import Flask
from flask_bootstrap import Bootstrap
app = Flask(__name__)


def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app

@app.route('/')
def index():
	index = '<h2>index page</h2>'
	return index

@app.route('/hello')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug = True)
