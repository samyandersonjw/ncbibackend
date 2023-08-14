from flask import Flask, request, redirect

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
  return redirect("https://www.ncbi.nlm.nih.gov/pmc/", code=302)
  
@app.route('/api/articles/<path:text>')
def index(text):
  if col.find_one({"id":999})["status"] == "good":
    entryID = request.path.split("/")[3]
    fullText = col.find_one({"id":int(entryID)})
    return fullText["fulltext"]
  else:
    return redirect("https://www.ncbi.nlm.nih.gov/pmc/", code=302)
