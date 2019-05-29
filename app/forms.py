from wtforms import Form, StringField

class ParkSearchForm(Form):
    search = StringField('')