from flask import Flask, render_template, url_for, request, redirect
from npsAPI import * 
app = Flask(__name__)

#Home Page
@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', api_key=api_key)

@app.route('/results/<state>')
def results(state):
    return render_template('results.html', webApp=webApp, value=state)

if __name__ == '__main__':
    app.run(debug=True)