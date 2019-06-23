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

# About Page
@app.route('/about')
def about():
        return render_template('about.html', title='About NPS')

# Results Page
@app.route('/results/<search>')
def results(search):
    if search in state.keys():
        parks = webApp.parksByState(search)
        term = state[search]
    else:
        search=search.data['search']
        parks = webApp.parksBySearch(search)
        term = '\'' + search + '\''
    return render_template('results.html', 
        webApp=webApp, 
        parks=parks, 
        term=term,
        title='Results for ' + '\'' + term + '\'')

# Park Profile Page
@app.route('/park/<parkCode>')
def park(parkCode):
    park = webApp.parkData(parkCode)[0]
    alerts = webApp.getParkAlerts(parkCode)
    return render_template('park.html', 
        webApp=webApp, 
        park=park, 
        alerts=alerts,
        title=park['name'])

# Articles Page
@app.route('/articles/<parkCode>')
def articles(parkCode):
    articles = webApp.getArticleData(parkCode)
    parkname = webApp.parkData(parkCode)[0]['name']
    return render_template('articles.html', 
        webApp=webApp, 
        articles=articles,
        parkname=parkname,
        title='Articles: ' + parkname)

# Campgrounds Page
@app.route('/campgrounds/<parkCode>')
def campgrounds(parkCode):
    campgrounds = webApp.getCampgroundData(parkCode)
    parkname = webApp.parkData(parkCode)[0]['name']
    return render_template('campgrounds.html', 
        webApp=webApp,
        campgrounds=campgrounds,
        parkname=parkname,
        title='Campgrounds: ' + parkname)

# Education Page
@app.route('/education/<parkCode>')
def education(parkCode):
	lessonPlans = webApp.getLessonData(parkCode)
	importantPeople = webApp.getPeopleData(parkCode)
	parkname = webApp.parkData(parkCode)[0]['name']
	return render_template('education.html',
		webApp=webApp,
		lessonPlans=lessonPlans,
		importantPeople=importantPeople,
		parkname=parkname,
		title='Education: ' + parkname)

# Events Page
@app.route('/events/<parkCode>')
def events(parkCode):
    events = webApp.getEventsData(parkCode)
    parkname = webApp.parkData(parkCode)[0]['name']
    return render_template('events.html', 
        webApp=webApp, 
        events=events,
        parkname=parkname,
        title='Events: ' + parkname)

# News Page
@app.route('/news/<parkCode>')
def news(parkCode):
    news = webApp.getNewsData(parkCode)
    parkname = webApp.parkData(parkCode)[0]['name']
    return render_template('news.html', 
        webApp=webApp, 
        news=news,
        parkname=parkname,
        title='News: ' + parkname)

# Visitor Centers Page
@app.route('/visitorcenters/<parkCode>')
def visitorcenters(parkCode):
    visitorcenters = webApp.getVisitorcentersData(parkCode)
    parkname = webApp.parkData(parkCode)[0]['name']
    return render_template('visitorcenters.html', 
        webApp=webApp, 
        visitorcenters=visitorcenters,
        parkname=parkname,
        title='Visitor Centers: ' + parkname)

# Runs Function
if __name__ == '__main__':
    app.run() 