# Authors : Gastone Pietro Rosati Papini
# Date    : 09/08/2022
# License : MIT
import math
import signal

from pydrivingsim import World
from scenarios import BasicSpeedLimit, BasicTrafficLight, OnlyVehicle, AutonomousVehicle


class GracefulKiller:
    kill_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, *args):
        self.kill_now = True


def main():
    # TO MODIFY THE SCENARIO
    # GOTO main_scenarios.py to change the end point and traffic light
    # GOTO agent.py to change the msg sent to the agent
    # av = OnlyVehicle()
    av = AutonomousVehicle()
    BasicTrafficLight()  #  can add extra trafficlights here
    BasicSpeedLimit()

    killer = GracefulKiller()
    while not killer.kill_now and World().loop:
        av.update()
        World().update()

    av.terminate()
    World().exit()


main()
