from calendar import monthrange

from .html import changeVal

def setStartTime(hour, minute):
    global time
    time = {
        "hour": hour,
        "minute": minute,
        "second": 0
    }

def setStartYear(year, month, day):
    global date
    date = {
        "year": year,
        "month": month,
        "day": day
    }

def addSecond():
    time["second"] += 1
    checkCorrectValue()

def checkCorrectValue():
    if time:
        if time["second"] >= 60:
            time["second"] -= 60
            time["minute"] += 1
        if time["minute"] >= 60:
            time["minute"] -= 60
            time["hour"] += 1
        if time["hour"] >= 24:
            time["hour"] -= 24
            if date: date["day"] += 1
    if date:
        if date["day"] > monthrange(date["year"], date["month"])[1]:
            date["day"] = 0
            date["month"] += 1
        if date["month"] > 12:
            date["month"] = 1
            date["year"] += 1

def updateTime():
    changeVal("year", date["year"])
    changeVal("month", date["month"])
    changeVal("day", date["day"])
    changeVal("hr", time["hour"])
    changeVal("hr", time["hour"])
    changeVal("min", time["minute"])
    changeVal("sec", time["second"])