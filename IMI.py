from time import ticks_ms
from pyb import RTC

rtc = RTC()
t1 = ticks_ms()
tz = rtc.datetime()
yea, mon, day, hou, minu, sec = tz[0],tz[1],tz[2],tz[4],tz[5],tz[6]

def timing_display():
    global yea, mon, day, hou, minu, sec, t1

    now = ticks_ms()
    delai = ((now - t1) // 1000)
    si = sec + delai
    t1 = now

    if si < 60:
        sec = si

    if (si >= 60) and (si < 3600):
        minu = minu + (si // 60)
        if minu >= 60:
            minu = minu - 60
            hou += 1
            if hou >= 60:
                hou = hou - 60
                day +=1
        sec = si - (60 * (si // 60)) 

    if (si >= 3600) and (si < 216000):
        hou = hou + (si // 3600)
        if hou >= 60:
            hou = hou - 60
            day += 1
        minu = minu + (si // 60)
        if minu >= 60:
            minu = minu - 60
            hou += 1
            if hou >= 60:
                hou = hou - 60
                day +=1
        sec = si - (60 *(si // 60))

    return hou, minu, sec

timing_display()
