# Fonction pour add Event Manuellement
def createManuelEvent(date,name,description) :
    event = Event()
    event.add(name, 'Awesome Meeting')
    #event.add('description', 'Define the roadmap of our awesome project')
    event.add('dtstart', datetime(2022, 1, 25, 8, 0, 0, tzinfo=pytz.utc))
    event.add('dtend', datetime(2022, 1, 25, 10, 0, 0, tzinfo=pytz.utc))
    

    organizer = vCalAddress('MAILTO:jdoe@example.com')
    

    organizer.params['name'] = vText('John Doe')
    organizer.params['role'] = vText('CEO')
    event['organizer'] = organizer
    event['location'] = vText('New York, USA')
    
    event['uid'] = '2022125T111010/272356262376@example.com'
    event.add('priority', 5)
    attendee = vCalAddress('MAILTO:rdoe@example.com')
    attendee.params['name'] = vText('Richard Roe')
    attendee.params['role'] = vText('REQ-PARTICIPANT')
    event.add('attendee', attendee, encode=0)
    
    attendee = vCalAddress('MAILTO:jsmith@example.com')
    attendee.params['name'] = vText('John Smith')
    attendee.params['role'] = vText('REQ-PARTICIPANT')
    event.add('attendee', attendee, encode=0)
    
    # Add the event to the calendar
    cal.add_component(event)