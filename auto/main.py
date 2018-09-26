import time
import logging

import krpc
import Kerbal

logging.basicConfig(format="%(message)s", level=logging.INFO)

target_speed = 10
connection = krpc.connect()
car = Kerbal.Car(connection)
logging.info("Simulation Started!")
run_time = 0
while run_time < 60:
    run_time += 1
    time.sleep(0.1)
    car.set_speed(target_speed)
car.brake()
logging.info("Simulation completed!")
