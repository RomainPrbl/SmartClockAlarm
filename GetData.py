import requests
from bs4 import BeautifulSoup
"""
url = "https://www.myefrei.fr/portal/student/planning"

reponse = requests.get(url)

if reponse.ok :
    soup = BeautifulSoup(reponse.text,features="html.parser")
    title = soup.find("title") 
    print(title.text)
    if title.text == "Efrei Paris - Connexion":
"""
with requests.Session() as s :
    url = "https://auth.myefrei.fr/uaa/interaction/4EAD6oHBH99Cj655y3YMm"
    url = "https://www.myefrei.fr/portal/student/planning"
    s.get(url)
    login_data = {"username" : "20210663","password" : "}Ro40/Pr35"}#"_csrf" : "0lZKvqX6-6rcXTM0oltDQH5kpxW83yBcy_Xk"
    s.post(url,data=login_data)
    r = s.get("https://www.myefrei.fr/portal/student/planning")
    print(r.text)
    soup = BeautifulSoup(r.text,features="html.parser")
    title = soup.find("title") 
    print(title.text)