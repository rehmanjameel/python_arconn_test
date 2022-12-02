from datetime import date, datetime, timezone, timedelta
import pytz
import testing
from suntime import Sun, SunTimeException
from suntimes import SunTimes
import sunriset
import astral, astral.sun

latitude = 30.1979793
longitude = 71.4724978
altitude = 0

tz_poland = pytz.timezone('asia/Pakistan')
tz_name = 'asia/Pakistan'
for_date = date(2022, 3, 25)

print('====== suntime ======')
abd = for_date
sun = Sun(latitude, longitude)
today_sr = sun.get_sunrise_time()
today_ss = sun.get_sunset_time()
print(today_sr.astimezone(tz_poland))
print(today_ss.astimezone(tz_poland))

print('====== suntimes ======')
sun2 = SunTimes(longitude=longitude, latitude=latitude, altitude=altitude)
day = datetime(for_date.year, for_date.month, for_date.day)
print(sun2.risewhere(day, tz_name))
print(sun2.setwhere(day, tz_name))

print('====== sunriset ======')
local = datetime.now()
utc = datetime.utcnow()
local_tz = float(((local - utc).days * 86400 + round((local - utc).seconds, -1))/3600)
number_of_years = 1
start_date = for_date
df = sunriset.to_pandas(start_date, latitude, longitude, 2, number_of_years)
for index, row in df.iterrows():
    print(row['Sunrise'])
    print(row['Sunset'])
    break

print('====== astral ======')
l = astral.LocationInfo('Custom Name', 'My Region', tz_name, latitude, longitude)
s = astral.sun.sun(l.observer, date=for_date)
print(s['sunrise'].astimezone(tz_poland))
print(s['sunset'].astimezone(tz_poland))