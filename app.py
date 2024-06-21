from flask import *
app = Flask(__name__)

@app.route("/murali", methods = ["GET", "POST"])
def murali():
    data = {
        "name" : "Murali",
        "company" : "Wipro",
        "sskill" : "New Relic APM"
    
    }
    return data

app.run()