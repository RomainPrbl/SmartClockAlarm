import pytz
# Fonction pour add Event Manuellement
def createManuelEvent(cal,dateStart,dateEnd,name,description) :
    event = Event()
    event.add(name, description)
    event.add('dtstart', datetime(dateStart[0], dateStart[1], dateStart[2], dateStart[3], 0, 0, tzinfo=pytz.utc))
    event.add('dtend', datetime(dateEnd[0], dateEnd[1], dateEnd[2], dateEnd[3], 0, 0, tzinfo=pytz.utc))
    cal.add_component(event)