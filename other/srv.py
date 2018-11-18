from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
import os
from time import strftime

exp_path = os.path.dirname(__file__)
app = Flask(__name__, template_folder=exp_path)
run_with_ngrok(app)

@app.route('/')
def experimentar():
    return render_template('experimento.html')

@app.route('/postdata', methods = ['POST'])
def get_data():
    data = request.form['data']
    
    with open(exp_path + '/data/' + str(strftime('%H-%M %j')) + ".txt", 'w') as out:
        out.write(data)

    return ''

if __name__ == '__main__':
    app.run()