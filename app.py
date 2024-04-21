from flask import Flask, render_template,  session, redirect, request, url_for, make_response
import os
from chat_bot.NN import get


IMG_FOLDER = os.path.join('static', 'images')
app = Flask(__name__)
app.config['IMG_FOLDER'] = IMG_FOLDER

@app.route('/',methods=["GET"])  
def homePage():
    return render_template("index.html")

@app.route('/farfadet_original.html',methods=["GET"])
def farfadet_original():
    return render_template("farfadet_original.html")

        

if __name__ == "__main__":
    app.run(debug=True)