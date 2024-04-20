
from flask import Flask, request, render_template

app = Flask(__name__)


# import hello_world from the hello_world.py
from hello_world import hello_world
from NN import get

@app.route('/')
def hello():
    return hello_world()

@app.route('/form', methods=['GET', 'POST'])
def form():
    output = ''
    if request.method == 'POST':
        # Retrieving the value from input box with name='input_name'
        input_value = request.form['input_name']
        #print(f'You entered: {input_value}')
        output = get(input_value)

        #return f'You entered: {input_value}'
    return render_template('form.html', output=output)