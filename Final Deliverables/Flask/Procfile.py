from flask import Flask
Procfile=Flask(__name__)
from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
  web: gunicorn app:app