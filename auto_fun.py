import threading
import sched, time
from datetime import date, datetime, timedelta
from suntime import Sun, SunTimeException

now = datetime.now()

run_at = now + timedelta(seconds=10)
delay = (run_at - now).total_seconds()

print(delay)
print(run_at)

s = sched.scheduler(time.time, time.sleep)
print("sle", time.sleep)


def print_time(a='default'):
    print("From print_time", time.time(), a)

    current_latitude1 = 30.1979793
    current_longitude1 = 71.4724978

    print("Latitude = ", current_latitude1)
    print("Longitude = ", current_longitude1)

    get_sun_time = Sun(current_latitude1, current_longitude1)

    today_date = date.today()

    sun_rise_time = get_sun_time.get_local_sunrise_time(today_date)
    sun_set_time = get_sun_time.get_local_sunset_time(today_date)

    print(sun_rise_time)
    print(sun_set_time)

    print('On {} the sun at Multan   raised at {} and get down at {}.'.
          format(today_date, sun_rise_time.strftime('%H:%M'), sun_set_time.strftime('%H:%M')))


s.enter(delay, 1, print_time)
s.run()
print(time.time())


# def print_some_times():
#     # print(time.time())
#     s.enter(delay, 1, print_time)
#     # s.enter(5, 2, print_time, argument=('positional',))
#     # s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
#     s.run()
#     print(time.time())
#
#
# print_some_times()


# while True:
#     s.enter(delay, 1, print_time)
#     s.run()
#     time.sleep(1)
