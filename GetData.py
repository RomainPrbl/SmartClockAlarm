import requests
from bs4 import BeautifulSoup
import icalendar 
import pytz
import datetime
from time import sleep,time



def obtenirLienPlanning():
    data = {}
    data["agenda_url"] = input("Collez le lien ici : ").strip().replace("webcal://", "https://")
    r = requests.get(data["agenda_url"])
    if r.status_code != 200:
        print("Erreur : Le lien que vous avez entré n'est pas valide.")
        obtenirLienPlanning()
    print(" ")
    return data

def passerDuLienAuCalendrier(data):
    r = requests.get(data["agenda_url"])
    cal = icalendar.Calendar.from_ical(r.content)
    return cal

def recupererLesEvents(calendar):

    current_utc = pytz.UTC.localize(datetime.datetime.utcnow())
    events = []
    for event in calendar.walk():
        if event.name == "VEVENT":
            start = event.get("dtstart").dt
            end = event.get("dtend").dt
            summary = event.get("summary")
            location = event.get("location")
            description = event.get("description")
            events.append(
                {"start": start, "end": end, "nom_cours": summary, "salle": location, "nom_prof": description})
    for event in events:
        if event["start"] > datetime.datetime.now(datetime.timezone.utc): # le datetime n'est pas naif !!!
            print(event["start"],event["nom_cours"],type(event["start"]))
            sleep(2)
    return None

if __name__ == "__main__":
    print(recupererLesEvents(passerDuLienAuCalendrier(obtenirLienPlanning())))

