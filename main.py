import time
from datetime import date, datetime, timedelta
import pytz
from geopy.geocoders import Nominatim
from suntime import Sun, SunTimeException
from astral import LocationInfo
from astral.sun import sun

# loc = Nominatim(user_agent="GetLoc")
#
# getLoc = loc.geocode("Multan")
#
# print(getLoc.address)

# current_latitude = getLoc.latitude
# current_longitude = getLoc.longitude

current_latitude = 30.1979793
current_longitude = 71.4724978

print("Latitude = ", current_latitude)
print("Longitude = ", current_longitude)

get_sun_time = Sun(current_latitude, current_longitude)

today_date = date.today()

sun_rise_time = get_sun_time.get_local_sunrise_time(today_date)
sun_set_time = get_sun_time.get_local_sunset_time(today_date)

print('On {} the sun at Multan   raised at {} and get down at {}.'.
      format(today_date, sun_rise_time.strftime('%H:%M'), sun_set_time.strftime('%H:%M')))


# city = LocationInfo(name="Multan", region="Pakistan", timezone='asia/Pakistan',
#                     latitude=current_latitude, longitude=current_longitude)
# print((
#     f"Information for {city.name}/{city.region}\n"
#     f"Timezone: {city.timezone}\n"
#     f"Latitude: {city.latitude:.02f}; Longitude: {city.longitude:.02f}\n"
# ))
# print(city)
#
# print(city.observer)
#
# s = sun(city.observer, date=datetime.now())
#
# print((
#     f'Dawn:    {s["dawn"]}\n'
#     f'Sunrise: {s["sunrise"]}\n'
#     f'Noon:    {s["noon"]}\n'
#     f'Sunset:  {s["sunset"]}\n'
#     f'Dusk:    {s["dusk"]}\n'))

current_date = date.today()
print("Current Date", current_date)
print(time.time())
now = datetime.now() + timedelta(hours=5)
print(now)

