import time
import logging
import krpc

import Kerbal
import Graph

logging.basicConfig(format="%(message)s", level=logging.INFO)

pid_start_values = [1, 0.1, 0.1, (-1, 1)]
target_speed = 2
simulation_lenght = 60
max_delta = 0.2
sleep_time = 0.1

connection = krpc.connect()
car = Kerbal.SimpleKerbalCar(connection, pid_start_values)
window = Graph.Window("Stats", "PID:" + str(pid_start_values))
speed_graph = window.add_graph("Speed")
target_speed_line = speed_graph.add_line("Target m/s")
actual_speed_line = speed_graph.add_line("Actual m/s")
delta_graph = window.add_graph("Change")
target_delta_line = delta_graph.add_line("Target Delta")
actual_delta_line = delta_graph.add_line("Actual Delta")
logging.info("Simulation Started!")

speed = 0
run_time = -1
while run_time < simulation_lenght:
    run_time += 1
    change = max_delta
    speed = speed + change
    if speed > target_speed:
        speed = target_speed
        change = 0
    target_speed_line.add_value(run_time, speed)
    target_delta_line.add_value(run_time, change)

run_time = -1
while run_time < simulation_lenght:
    run_time += 1
    time.sleep(sleep_time)
    change = car.set_speed(target_speed)
    actual_speed_line.add_value(run_time, car.speed())
    actual_delta_line.add_value(run_time, change)

car.brake()
window.render()
logging.info("Simulation completed!")
