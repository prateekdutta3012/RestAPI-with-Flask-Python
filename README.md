# Python-API_Flask

pip install flask

from flask import Flask 

app=Flask(__name__)

@app.route('/')

def home():

   return "Hey, This is Prateek!"

app.run(port=5000)

cd~/directory where file is saved/

python "file name"
