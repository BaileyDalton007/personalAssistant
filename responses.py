from datetime import datetime
from pytz import timezone

eastern = timezone('US/Eastern')

def getToday():
    fmt = '%Y-%m-%d 00:00:00'
    loc_dt = eastern.localize(datetime.now())
    dt = loc_dt.strftime(fmt)
    return dt

def todayEvents(data):
    output = ""

    # My best attempt at making the response sound somewhat natural
    if len(data) > 1:
        output = "You have " + str(len(data)) + " events today. There is "
        for i in range(len(data) - 1):
            output = output + data[i].name[0] + ", "
        
        output = output + "and " + data[len(data) - 1].name[0] + ". "

    elif len(data) == 1:
        output = "Your only event today is " + data[0].name[0] + ". "
    else:
        output = "You have no events today."
    
    return output

def tomorrowEvents(data):
    output = ""

    # My best attempt at making the response sound somewhat natural
    if len(data) > 1:
        output = "You have " + str(len(data)) + " events tomorrow. There is "
        for i in range(len(data) - 1):
            output = output + data[i].name[0] + ", "
        
        output = output + "and " + data[len(data) - 1].name[0] + ". "
    elif len(data) == 1:
        output = "Your only event tomorrow is " + data[0].name[0] + ". "
    else:
        output = "You have no events tomorrow."
    
    return output



