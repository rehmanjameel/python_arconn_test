import datetime
import time

get_now = datetime.datetime.now()
print("now", get_now)
from scheduler import Scheduler
import scheduler.trigger as trigger

# def foo():
# print("foo")


# schedule = Scheduler()

# schedule.cyclic(datetime.timedelta(seconds=10), foo)
# schedule.minutely(datetime.time(second=10), foo)
# schedule.daily(datetime.time(second=10), foo)
# schedule.exec_jobs()

# print(schedule)
#
# while True:
#     schedule.exec_jobs()
#     time.sleep(1)

import sched
from datetime import date, datetime, timedelta
from suntime import Sun, SunTimeException

now = datetime.now()
form = now.strftime("%Y-%m-%d %I:%M")
print("For", form)
print("Forms", now)
print("time", time.time())
run_at = now + timedelta(seconds=3)
delay = (run_at - now).total_seconds()

print(delay)
print(run_at)

s = sched.scheduler(time.time, time.sleep)
print(s)

sun_rise_time = None
sun_set_time = None


def light_on():
    pass


def light_off():
    pass


def do_something(sec):
    # do your stuff

    current_latitude1 = 30.1979793
    current_longitude1 = 71.4724978

    print("Latitude = ", current_latitude1)
    print("Longitude = ", current_longitude1)

    get_sun_time = Sun(current_latitude1, current_longitude1)

    today_date = datetime.today()
    print("today", today_date)
    global sun_rise_time
    global sun_set_time

    sun_rise_time = get_sun_time.get_local_sunrise_time(today_date)
    sun_set_time = get_sun_time.get_local_sunset_time(today_date)
    forms = sun_set_time.strftime("%Y-%m-%d %H:%M")

    t = sun_set_time.timestamp()
    print("t", t)
    print("Sun", sun_rise_time)
    print("Formsss", forms)
    print("Formsss", sun_set_time)

    print('On {} the sun at Multan   raised at {} and get down at {}.'.
          format(today_date, sun_rise_time.strftime('%H:%M'), sun_set_time.strftime('%H:%M')))
    s.enter(delay, 1, do_something, (sec,))


s.enter(delay, 1, do_something, (s,))
s.run()
