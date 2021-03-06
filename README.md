# National Park Service Information Kiosk (Winner)
A deployed web application that makes use of the NPS Data API in order to function as an Information Kiosk for the National Park Service.

Access the site here: https://npskioskdfel.herokuapp.com/

This web application is a submission for the semifinalist round of the August 2019 Software Enginereering Summit hosted by Capital One.

View the MindSumo challenge criteria [here](https://www.mindsumo.com/contests/national-park-api?utm_campaign=solution_received_notification&utm_source=mindsumo&utm_medium=email)
## Demo
![](/static/demo/Demo.gif)

## Built With  
- HTML/CSS
- Flask

## API Reference
- [NPS Data API](https://www.nps.gov/subjects/developer/index.htm)

## Run Application on Local Machine
With Flask installed on your device, please run the following:

- Unix Bash (Linux, Mac, etc.):
```
$ export FLASK_APP=nps
$ flask run
```
- Windows CMD:
```
> set FLASK_APP=nps
> flask run
```
- Windows PowerShell
```
> $env:FLASK_APP = "nps"
> flask run
```
In your browser enter: localhost:5000
