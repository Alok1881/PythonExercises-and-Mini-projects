'''
You have a list of events that indicate when users log in and log out of machines.
 Each event is represented as an instance of the Event class, which has the following attributes:
- date: a string representing the date and time of the event in the format 'YYYY-MM-DD HH:MM:SS 
- type: a string that is either 'login' or 'logout', indicating the type of event
- machine: a string representing the name of the machine on which the event occurred
- user: a string representing the name of the user who logged in or out
Write a function called current_users that takes a list of Event instances 
and returns a dictionary mapping machine names to sets of currently logged-in users. 
The function should process the events in chronological order, 
updating the sets of logged-in users for each machine based on the login and logout events.'''

def get_event_date(event):
  return event.date

def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout":
        
        if event.user not in machines[event.machine]:
            pass
        else:
            machines[event.machine].remove(event.user)
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))

class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user


events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)
generate_report(users)