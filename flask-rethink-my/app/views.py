from flask import render_template, url_for, redirect, g
from app import app
from forms import TaskForm

@app.route("/")
def index():
    form = TaskForm()
    return render_template('index.html', form=form)

#rethink imports
import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError
# rethink config
RDB_HOST =  'localhost'
RDB_PORT = 28015
TODO_DB = 'todo'
# db setup; only run once
def dbSetup():
  connection = r.connect(host=RDB_HOST, port=RDB_PORT)
  try:
      r.db_create(TODO_DB).run(connection)
      r.db(TODO_DB).table_create('todos').run(connection)
      print 'Database setup completed'
  except RqlRuntimeError:
      print 'Database already exists.'
  finally:
      connection.close()
dbSetup()
# open connection before each request
@app.before_request
def before_request():
  try:
      g.rdb_conn = r.connect(host=RDB_HOST, port=RDB_PORT, db=TODO_DB)
  except RqlDriverError:
      abort(503, "Database connection could be established.")
# close the connection after each request
@app.teardown_request
def teardown_request(exception):
  try:
      g.rdb_conn.close()
  except AttributeError:
      pass