
from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
import json

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.todo_db
collection = db.todos


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api")
def api():
    with open("data.json") as f:
        data = json.load(f)
    return jsonify(data)

# Backend route for todo submission 


@app.route("/submittodoitem", methods=["POST"])
def submit_todo():
    data = {
        "itemName": request.form.get("itemName"),
        "itemDescription": request.form.get("itemDescription")
    }

    collection.insert_one(data)

    return "Todo Submitted"


if __name__=="__main__":
    app.run(debug=True)


