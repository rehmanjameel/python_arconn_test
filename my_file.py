from sconn.sched_test import SConn
from sconn.autobahn_test import Component
from autobahn.twisted.wamp import ApplicationRunner


def main():
    scon = SConn()
    scon.light_on_off()
    scon.start()
    runner = ApplicationRunner("ws://0.0.0.0:8080/ws", realm="realm1")
    runner.run(Component)


if __name__ == '__main__':
    main()
