from calendar import month
from datetime import datetime
import re

date=datetime.now()
years=date.year
months=date.month
days=date.day
hours=date.hour
minutes=date.minute

def verifDate(dateToGet) :
    newdate=datetime.now()
    if(dateToGet==newdate) :
        return 1
    else : 
        return 0


