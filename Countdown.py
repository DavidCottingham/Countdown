import datetime, time

def check_complete(time_diff):
    pause_seconds_before_exit = 6
    
    if (time_diff.days == 0 and time_diff.seconds <= 0) or time_diff.days < 0:
        print("\n\nCountdown Complete!")
        time.sleep(pause_seconds_before_exit)
        return True

def init():
    print("Countdown!")
    year = 2016
    month = 2
    day = 2
    hour = 20
    minute = 50

    while True:
        diff = datetime.datetime(year, month, day, hour, minute) - \
               datetime.datetime.now()           
        hours, remainder = divmod(diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        if check_complete(diff):
            break
        print("Countdown will comeplete in", diff.days, "days,", hours,"hours,",
              minutes, "minutes, and", seconds, "seconds!", end='\r')
        time.sleep(1)

init()
