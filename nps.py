from flask import Flask, render_template, url_for, request, redirect
from npsAPI import * 
from forms import ParkSearchForm

app = Flask(__name__, template_folder='templates')

# Home Page
@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    search = ParkSearchForm(request.form)
    if request.method == 'POST':
        return results(search)
    return render_template('home.html', 
        api_key=api_key, 
        form=search)

# Results Page
@app.route('/results/<search>')
def results(search):
    if search in state.keys():
        parks = webApp.parksByState(search)
        term = state[search]
    else:
        search=search.data['search']
        parks = webApp.parksBySearch(search)
        term = search
    return render_template('results.html', 
        webApp=webApp, 
        parks=parks, 
        term=term)

# Park Profile Page
@app.route('/park/<parkCode>')
def park(parkCode):
    park = webApp.parkData(parkCode)[0]
    alerts = webApp.getParkAlerts(parkCode)
    return render_template('park.html', 
        webApp=webApp, 
        park=park, 
        alerts=alerts,)

# Articles Page
@app.route('/articles/<parkCode>')
def articles(parkCode):
    articles = webApp.getArticleData(parkCode)
    parkname = webApp.parkData(parkCode)[0]['name']
    return render_template('articles.html', 
        webApp=webApp, 
        articles=articles,
        parkname=parkname)

# Campgrounds Page
@app.route('/campgrounds/<parkCode>')
def campgrounds(parkCode):
    campgrounds = webApp.getCampgroundData(parkCode)
    parkname = webApp.parkData(parkCode)[0]['name']
    return render_template('campgrounds.html', 
        webApp=webApp,
        campgrounds=campgrounds,
        parkname=parkname)

# Events Page
@app.route('/events/<parkCode>')
def events(parkCode):
    events = webApp.getEventsData(parkCode)
    parkname = webApp.parkData(parkCode)[0]['name']
    return render_template('events.html', 
        webApp=webApp, 
        events=events,
        parkname=parkname)

# News Page
@app.route('/news/<parkCode>')
def news(parkCode):
    news = webApp.getNewsData(parkCode)
    parkname = webApp.parkData(parkCode)[0]['name']
    return render_template('news.html', 
        webApp=webApp, 
        news=news,
        parkname=parkname)

# Visitor Centers Page
@app.route('/visitorcenters/<parkCode>')
def visitorcenters(parkCode):
    visitorcenters = webApp.getVisitorcentersData(parkCode)
    parkname = webApp.parkData(parkCode)[0]['name']
    return render_template('visitorcenters.html', 
        webApp=webApp, 
        visitorcenters=visitorcenters,
        parkname=parkname)

# Runs Function
if __name__ == '__main__':
    app.run(debug=True) 