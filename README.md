# Python-API_Flask

pip install flask

---------------------

from flask import Flask 

app=Flask(__name__)

@app.route('/')

def home():

   return "Hey, This is Prateek!"

app.run(port=5000)

----------------------------------

cd~/directory where file is saved/

python "file name"

-------------------------

post:- used to recieve data.

Get :- used to send data back.

--------------
End point creating

from flask import Flask,jsonify 

app=Flask(__name__)

stores=[
    {
        'name':'My Personalized store',
        'item':[
            {
                'name':'Notebook-Classmate',
                'price': 40.00
            }
        ]
    }
]

# POST /store data: {name:}
@app.route('/store',methods=['POST'])
def create_store():
    pass 

#GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    pass

#GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})

#POST/store/<string:name>/item{name:,price}
@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    pass 

#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass 

app.run(port=5000)
