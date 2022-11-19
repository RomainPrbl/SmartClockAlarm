import requests
from bs4 import BeautifulSoup
import icalendar 
import pytz
import datetime
from time import sleep

CONFIG = {}

def recuperer_planing():
    print("======== PLANNING MYEFREI ========")
    print("Veuillez vous rendre sur votre planning MyEfrei (https://www.myefrei.fr/portal/student/planning)")
    print("Et cliquer sur le bouton \"COPIER URL PLANNING (ICAL)\"")
    CONFIG["agenda_url"] = input("Puis collez le lien ici : ").strip().replace("webcal://", "https://")
    r = requests.get(CONFIG["agenda_url"])
    if r.status_code != 200:
        print("Erreur : Le lien que vous avez entré n'est pas valide.")
        recuperer_planing()
    print(" ")

def get_agenda_():
    r = requests.get(CONFIG["agenda_url"])
    cal = icalendar.Calendar.from_ical(r.content)
    return cal

def get_current_event(calendar):
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
        print(event)
        sleep(5)
        if event["start"] < current_utc < event["end"]:
            return event
    print("ICIIIIIIIIIIIIII",event)
    return None

if __name__ == "__main__":
    recuperer_planing()
    print(get_current_event(get_agenda_()))








"""
s=requests.Session()
url = "https://www.myefrei.fr/portal/student/planning"
rget = s.get(url)

token = re.search("name=\"_recherche_recherchertype\[_token\]\" value=\"([a-z0-9]{40})\"", rget.text).group(1)
payload = {"_recherche_recherchertype[_token]": token}

login_data = {"username" : "20210663","password" : "}Ro40/Pr35","_csrf" : str(token)}
print(token,type(token))

s.post(url,data=login_data)

r = s.get("https://www.myefrei.fr/portal/student/planning")
print(r.text)
soup = BeautifulSoup(r.text,features="html.parser")
title = soup.find("title") 
print(title.text)
"""
