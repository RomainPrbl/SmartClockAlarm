from playsound import playsound

def alarme(son) :
    playsound(f'D:/projetAlarme/SmartClockAlarm/assets/{son}.mp3')

alarme("sonReveilStandard")