import json
from flask import Flask, render_template, request
import os
from model import predictor;

app = Flask(__name__)

path_file = os.getcwd()
path_final_name = path_file + '/static/'


@app.route("/", methods=["GET","POST"])
def index():
    if(request.method == "GET") :
        return render_template('index.html')
    elif (request.method == 'POST') :
        # print(request.json)  
        # return "true"
        authorName = request.json['authorName']
        title = request.json['title']
        text = "  "
        res = predictor(author=authorName,title=title,text=text)
       
        if(res) : return "true"
        else : return "false"

app.run(debug=True)
