import requests
from bs4 import BeautifulSoup
import re 

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