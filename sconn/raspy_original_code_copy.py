import time
import sched
from datetime import datetime, timedelta

from suntime import Sun

# from arconn.gpio_control import GPIO_OUT_OFF, GPIO_OUT_ON, set_out_high, set_out_low

sun_set_seconds = None
sun_rise_seconds = None

light_scheduler = sched.scheduler(time.time, time.sleep)
now = datetime.now()

run_at = now + timedelta(hours=12)
delay = (run_at - now).total_seconds()


def get_sun_timings():
    current_latitude1 = 30.1979793
    current_longitude1 = 71.4724978

    get_sun_time = Sun(current_latitude1, current_longitude1)
    # current date time
    today_date = datetime.today()

    sun_rise_time = get_sun_time.get_local_sunrise_time(today_date)
    sun_set_time = get_sun_time.get_local_sunset_time(today_date) - timedelta(hours=5)
    print(sun_set_time)

    global sun_set_seconds
    global sun_rise_seconds

    sun_set_seconds = sun_set_time.timestamp()
    sun_rise_seconds = sun_rise_time.timestamp()


def light_on_off(time_):
    get_sun_timings()
    light_scheduler.enter(delay, 1, light_on_off, (time_,))


def light_on(time_):
    print("on")
    # set_out_high(20)
    light_scheduler.enterabs(sun_set_seconds, 1, light_on, (time_,))


def light_off(time_):
    # set_out_low(20)
    light_scheduler.enterabs(sun_rise_seconds, 1, light_off, (time_,))


class ARConn:
    try:
        time_ = light_scheduler

        # getting  sun set and rise time in seconds to set the scheduler
        get_sun_timings()

        def __init__(self, time_):
            self.time = time_

        # Scheduling sun set and rise time
        light_scheduler.enter(delay, 1, light_on_off, (light_scheduler,))
        # Scheduling light on
        light_scheduler.enterabs(sun_set_seconds, 1, light_on, (light_scheduler,))
        # Scheduling light off
        light_scheduler.enterabs(sun_rise_seconds, 1, light_off, (light_scheduler,))
        # Running scheduler
        # s.repeat_on_days('MTWTFss', time(14, 51), 0, job, 3)

        light_scheduler.run()
    finally:
        print("Closed")


"""
set_hours = sun_timings.sun_set_hours
set_minutes = sun_timings.sun_set_minutes
rise_hours = sun_timings.sun_rise_hours
rise_minutes = sun_timings.sun_rise_minutes
"""

# def get_sun_timings():
#     current_latitude1 = 30.1979793
#     current_longitude1 = 71.4724978
#
#     get_sun_time = Sun(current_latitude1, current_longitude1)
#     # current date time
#     today_date = datetime.today()
#
#     sun_rise_time = get_sun_time.get_local_sunrise_time(today_date)
#     sun_set_time = get_sun_time.get_local_sunset_time(today_date)
#     print(sun_set_time)
#
#     global sun_set_hours
#     global sun_set_minutes
#     global sun_rise_hours
#     global sun_rise_minutes
#
#     sun_set_hours = sun_set_time.strftime("%H")
#     sun_set_minutes = sun_set_time.strftime("%M")
#     sun_rise_hours = sun_rise_time.strftime("%I")
#     sun_rise_minutes = sun_rise_time.strftime("%M")
