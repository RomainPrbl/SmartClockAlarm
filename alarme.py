from playsound import playsound
from gestionTemps import verifDate

def alarme(son) :
    playsound(f'D:/projetAlarme/SmartClockAlarm/assets/{son}.mp3')

alarme("sonMilitaire")


def alarmeIfTime(dateToGet) :
       if(verifDate(dateToGet)) :
        alarme("sonReveilStandar")

       
    