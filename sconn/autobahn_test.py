from autobahn.twisted.wamp import ApplicationSession
from sconn.sched_test import light_on, light_off


class Component(ApplicationSession):
    async def onJoin(self, details):
        def on_event(msg):
            print("Go event: {}".format(msg))
            if msg == "On":
                light_on()
            if msg == "Off":
                light_off()

        await self.subscribe(on_event, 'org.codebase')
        print("subscribed")
