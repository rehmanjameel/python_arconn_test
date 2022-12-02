import time
import timesched
from datetime import date, datetime, timedelta, time
from suntime import Sun
import asyncio
from sqlitedict import SqliteDict
from autobahn.twisted.wamp import ApplicationSession

# now = datetime.now()
#
# run_at = now + timedelta(seconds=10)

# print("run", run_at)
# delay = (run_at - now).total_seconds()
# print("run1", timing.delay)


def light_off():
    print("light off")


def light_on():
    print("light on")


class SConn:
    light_scheduler = timesched.Scheduler()
    time_db = SqliteDict("suntime.sqlite", tablename="table_sun_time", autocommit=True)

    def light_on_off(self):
        current_latitude1 = 30.1979793
        current_longitude1 = 71.4724978

        """suntime library to get the sun timing according to current location"""
        get_sun_time = Sun(current_latitude1, current_longitude1)
        # current date time
        today_date = datetime.today()

        """methods to get the """
        sun_rise_time = get_sun_time.get_local_sunrise_time(today_date)
        sun_set_time = get_sun_time.get_local_sunset_time(today_date)

        """string formatted sun set and rise time in hours and minutes
        here 'H' for pm and 'I' for am hours"""

        sun_set_hours = sun_set_time.strftime("%H")
        sun_set_minutes = sun_set_time.strftime("%M")
        sun_rise_hours = sun_rise_time.strftime("%I")
        sun_rise_minutes = sun_rise_time.strftime("%M")

        self.time_db["1"] = {"sun_set_hours": sun_set_hours, "sun_set_minutes": sun_set_minutes,
                             "sun_rise_hours": sun_rise_hours, "sun_rise_minutes": sun_rise_minutes}

        for key, items in self.time_db.items():
            print("%s=%s" % (key, items))
        print(self.time_db)
        self.time_db.close()

        """function scheduling the light timing on week days excluding sunday
         as 's' for sunday is in lower case"""

        self.light_scheduler.repeat_on_days('MTWTFSs', time(15, 42), 0, light_on)
        self.light_scheduler.repeat_on_days('MTWTFSs', time(15, 43), 0, light_off)

    def start(self):
        """Scheduling sun set and rise time using timesched repeat_on_days method taking arguments as
            (days from Mon-Sat [sunday not included], time(hours, minutes), priority, func_name)
            it's time format is 24 hours"""

        try:
            async def scheduling_day_sec(timeout, light_on_off):
                await asyncio.sleep(timeout)
                await light_on_off()
            task = asyncio.create_task(scheduling_day_sec(3600, self.light_on_off))
            # self.light_scheduler.repeat_on_days('MTWTFSs', time(15, 46), 0, self.light_on_off)
            # self.light_scheduler.run()

        finally:
            print("Closed")
