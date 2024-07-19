from flask import Flask, render_template, request

app = Flask(__name__)

import google.generativeai as palm
import os

api = os.getenv("MAKERSUITE_API_TOKEN")
palm.configure(api_key=api)
model = {"model":"models/chat-bison-001"}

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/generative-ai",methods=["GET","POST"])
def generative_ai():
    q = request.form.get("q")
    r = palm.chat(**model, messages=q)
    return(render_template("generative-ai.html", r=r.last))

@app.route("/dapp-add-value",methods=["GET","POST"])
def dapp_add_value():
    return(render_template("index.html"))

if __name__ == "__main__":
    app.run()
