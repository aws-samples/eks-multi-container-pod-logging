# import files
from flask import Flask, render_template, request, session, url_for, redirect, jsonify
from datetime import datetime
import uuid
import logging


logging.basicConfig(filename='data/example.log', level=logging.INFO)

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"Status" : "Ok"})


@app.route("/health")
def health():
    return jsonify({"Status" : "Ok"})


@app.route("/log")
def log():

    for i in range(6):
        random_string = lowercase_str = uuid.uuid4().hex
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        log_message = f"This is the new log message generated {random_string} at {dt_string}"
        logging.info(log_message)
        
    return jsonify({"Status" : "Ok"})


if __name__ == "__main__": 
    app.run(debug=True, host='0.0.0.0')