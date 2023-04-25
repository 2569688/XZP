import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        minutes, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(minutes, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print('Time is up!')

countdown(30) # replace 30 with the number of minutes you want the timer to run for
