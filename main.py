from flask import Flask, request

app = Flask(__name__)
#byuvinc2:RnjcHsPi03kMa9e2
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://byuvinc2:RnjcHsPi03kMa9e2@cluster0.yenjypm.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["db"]
col = db["dbmain"]

@app.route("/")
def hello():
  return "Hello", 200
@app.route('/api/articles/<path:text>')
def index(text):
  entryID = request.path.split("/")[3]
  fullText = col.find_one({"id":int(entryID)})
  return fullText["fulltext"]

app.run(host='0.0.0.0', port=80)
