import datetime as dt
from time import sleep

t = dt.datetime.now()
minute_count = 0

while True:
    current_time = dt.datetime.now()
    current_time_24 = current_time.strftime("%Y-%m-%d %H:%M")
    print("Curr", current_time)
    current_time_12 = current_time.strftime("%Y-%m-%d %I:%M")

    print(current_time_12)
    print(current_time_24)

    # delta_minutes = (dt.datetime.now() -t).seconds
    # if delta_minutes and delta_minutes != minute_count:
    #     print("1 Min has passed since the last print")
    #     minute_count = delta_minutes
    # sleep(1) # Stop maxing out CPU
