import requests
from bs4 import BeautifulSoup
import icalendar 
import pytz
import datetime
from time import sleep,time

def recupLienDuTxt():
    f = open("lien.txt","r")
    lines = f.readlines()
    f.close()
    if len(lines) == 0:
        print("Pas de lien !")
        return None
    return lines[0]

def obtenirLienPlanning():
    data = {}
    data["agenda_url"] =recupLienDuTxt().strip().replace("webcal://", "https://")
    r = requests.get(data["agenda_url"])
    if r.status_code != 200:
        print("Erreur : Le lien que vous avez entré n'est pas valide.")
        #obtenirLienPlanning()
        return None
    return data

def passerDuLienAuCalendrier(data):
    r = requests.get(data["agenda_url"])
    cal = icalendar.Calendar.from_ical(r.content)
    return cal

def recupererLesEvents(calendar):
    current_utc = pytz.UTC.localize(datetime.datetime.utcnow())
    events = []
    eventaVenir = []
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
            eventaVenir.append(event)
    return eventaVenir

def estDejaRempli():
    # 0 fichier vide 1 sinon 
    f = open("events.txt","r")
    lines = f.readlines()
    f.close
    if len(lines) == 0 : 
        return 0
    else :
        return 1

def writeEventsInTxt(events):
    f = open("events.txt","w") 
    for dico in events :
        f.write(str(dico) + '\n')
    f.close()

def recupererLeProchainCours():
    event = recupererLesEvents(passerDuLienAuCalendrier(obtenirLienPlanning()))
    return event[0]

def tempsAvantLeProchainCours(dicoEvent):
    pass

def convertirDateDigiEnPhrase(datetime):
    """
    passer de 18/01/2003 à 18 janvier 2003 
    """
    mois = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre",
    "octobre","novembre","decembre"]
    return str(datetime.day,' ',mois[datetime.month],' ',datetime.year)

if __name__ == "__main__":
    start = recupererLeProchainCours()["start"]
    print(convertirDateDigiEnPhrase(start))

