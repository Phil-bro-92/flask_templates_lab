from flask import render_template, request  # ADDED
from app import app
from models.event_list import events, add_new_event
from models.event import Event
from datetime import datetime

@app.route('/events')
def get_all_events():
    return render_template("index.html", title="home", events = events)

@app.route('/events', methods=["POST"])
def add_event():
    event_name = request.form["event_name"]
    year = datetime.strptime(request.form["event_date"], '%Y-%m-%d').year
    month = datetime.strptime(request.form["event_date"], '%Y-%m-%d').month
    day = datetime.strptime(request.form["event_date"], '%Y-%m-%d').day
    room = request.form['room']
    description = request.form['description']
    number_of_guests = request.form['number_of_guests']
    new_event = Event(year, month, day, event_name, number_of_guests, room, description)
    add_new_event(new_event)
    print(type(year))
    return render_template("index.html", title="Home", events = events)
    
