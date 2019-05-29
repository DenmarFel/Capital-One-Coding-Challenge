from flask import Flask, render_template, url_for, request, redirect
from npsAPI import * 
from forms import ParkSearchForm
app = Flask(__name__, template_folder='templates')

#Home Page
@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    search = ParkSearchForm(request.form)
    if request.method == 'POST':
        return searchresults(search)
    return render_template('home.html', api_key=api_key, form=search)

@app.route('/results/<state>')
def results(state):
    return render_template('results.html', webApp=webApp, value=state)

@app.route('/searchresults/<q>')
def searchresults(search):
    q = search.data['search']
    return render_template('searchresults.html', webApp=webApp, q=q)

@app.route('/park/<parkCode>')
def park(parkCode):
	return render_template('park.html', webApp=webApp, value=parkCode)

if __name__ == '__main__':
    app.run(debug=True) 