from models.event import *

event_1 = Event(1992, 2, 4, "Birthday", 12, "The Hall", "Party!", True  )
event_2 = Event(2009, 5, 8, "another birthday", 30, "Cinema", "Movie", False)
events = [event_1, event_2]

def add_new_event(new_event):
    events.append(new_event)
