import time
import logging

import krpc
import Kerbal

logging.basicConfig(format="%(message)s",level=logging.INFO)

target_speed = 5
connection = krpc.connect()
car = Kerbal.Car(connection)
logging.info("Simulation Started!")
run_time = 0
while run_time < 3000:
    run_time += 1
    time.sleep(0.01)
    speed = car.speed()
    logging.info("Speed: " + str(speed))
    car.set_speed(target_speed)
logging.info("Simulation completed!")
