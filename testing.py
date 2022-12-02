# import datetime
# import time
#
# while True:
#     print(datetime.datetime.now().strftime("%H:%M:%S"))
#     time.sleep(5)
# def clock():
#
#
#
# clock()
import datetime
from suntime import Sun, SunTimeException

latitude = 30.1979793
longitude = 71.4724978

sun = Sun(latitude, longitude)

# Get today's sunrise and sunset in UTC
today_sr = sun.get_sunrise_time()
today_ss = sun.get_sunset_time()
print('Today at Warsaw the sun raised at {} and get down at {} UTC'.
      format(today_sr.strftime('%H:%M'), today_ss.strftime('%H:%M')))

# On a special date in your machine's local time zone
abd = datetime.date(2022, 3, 25)
abd_sr = sun.get_local_sunrise_time(abd)
abd_ss = sun.get_local_sunset_time(abd)
print('On {} the sun at Warsaw raised at {} and get down at {}.'.
      format(abd, abd_sr.strftime('%H:%M'), abd_ss.strftime('%H:%M')))

# Error handling (no sunset or sunrise on given location)
latitude = 87.55
longitude = 0.1
sun = Sun(latitude, longitude)
try:
    abd_sr = sun.get_local_sunrise_time(abd)
    abd_ss = sun.get_local_sunset_time(abd)
    print('On {} at somewhere in the north the sun raised at {} and get down at {}.'.
          format(abd, abd_sr.strftime('%H:%M'), abd_ss.strftime('%H:%M')))
except SunTimeException as e:
    print("Error: {0}.".format(e))