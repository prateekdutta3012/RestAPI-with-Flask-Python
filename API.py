from flask import Flask 
app=Flask(__name__)
@app.route('/')
def home():
    return "Hey, This is Prateek!"

app.run(port=5000)
