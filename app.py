from flask import Flask, render_template,  session, redirect, request, url_for
import os
from NN import get


IMG_FOLDER = os.path.join('static', 'images')
app = Flask(__name__)
app.config['IMG_FOLDER'] = IMG_FOLDER

@app.route('/',methods=["GET"])  
def homePage():
    return render_template("index.html")

@app.route('/chat_bot.html',methods=["GET","POST"])
def show_index():
    output = ''
    if request.method == 'POST':
        # Retrieving the value from input box with name='input_name'
        input_value = request.form['input_name']
        print(f'You entered: {input_value}')
        output = get(input_value)

        #return f'You entered: {input_value}'
    return render_template('chat_bot.html', output=output)

if __name__ == "__main__":
    app.run(debug=True)