from flask import Flask, render_template, url_for
import datetime


app = Flask(__name__)

days = {1:'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
months = {
 1: 'January',
 2: 'February',
 3: 'March',
 4: 'April',
 5: 'May',
 6: 'June',
 7: 'July',
 8: 'August',
 9: 'September',
 10: 'October',
 11: 'November',
 12: 'December'
}


date = datetime.datetime.now().day

def suffix(date):
    date_suffix = ["th", "st", "nd", "rd"]

    if date % 10 in [1, 2, 3] and date not in [11, 12, 13]:
        return date_suffix[date % 10]
    else:
        return date_suffix[0]

dateSuffix = suffix(date)

def dateTime():
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    day = datetime.datetime.now().isoweekday()
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    current = datetime.datetime.now().year
    return hour, minute, second, day, month, year, current

@app.route('/')
def index():
    x = dateTime()
    return render_template('index.html', hour=x[0], current=x, day=x, date=date, month=x, days=days, months=months, year=x, minute=x, second=x, suffix=dateSuffix)

@app.route('/user/<name>')
def greet(name):
    x = dateTime()
    return render_template('index.html', name=name, hour=x[0], current=x, day=x, date=date, month=x, days=days, months=months, year=x, minute=x, second=x, suffix=dateSuffix)
 
if __name__ == '__main__':
    app.run(debug=True)
