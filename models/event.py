from datetime import date
class Event:
    def __init__(self, year, month, day, event_name, number_of_guests, room, description, recurring):
        self.event_date = date(year, month, day)
        self.event_name = event_name
        self.number_of_guests = number_of_guests
        self.room = room
        self.description = description
        self.recurring = recurring
