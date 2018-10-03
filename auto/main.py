import time
import logging

import Kerbal
import Graph

logging.basicConfig(format="%(message)s", level=logging.INFO)

pid_start_values = [1, 0.1, 0.1, (-1, 1)]
target_speed = 10
simulation_lenght = 200
sleep_time = 0.1
accuracy = 0.1

kerbal = Kerbal.Kerbal()

car = Kerbal.SimpleKerbalCar(kerbal, pid_start_values)
window = Graph.Window("Stats", "PID:" + str(pid_start_values))
speed_graph = window.add_graph("Speed")
target_speed_line = speed_graph.add_line("Target m/s")
actual_speed_line = speed_graph.add_line("Actual m/s")
delta_graph = window.add_graph("Delta")
target_delta_line = delta_graph.add_line("Target Delta")
actual_delta_line = delta_graph.add_line("Actual Delta")
change_graph = window.add_graph("Change", False)
change_line = change_graph.add_line("Change")

logging.info("Simulation Started!")
kerbal.reset()
kerbal.text("Finding Max Delta!")
max_delta = car.findMaxAcc(target_speed, sleep_time, accuracy=accuracy)
kerbal.text("Finding Delta for target Speed: " + str(target_speed))
delta_for_target_speed = car.findAccForSpeed(target_speed, sleep_time, accuracy=accuracy)
kerbal.reset()

# Simulation run
speed = 0
delta = 0
run_time = -1
while run_time < simulation_lenght:
    run_time += 1
    delta = max_delta
    speed = speed + delta
    if speed > target_speed:
        speed = target_speed
        delta = delta_for_target_speed
    target_speed_line.add_value(run_time, speed)
    target_delta_line.add_value(run_time, delta)

# Test run
kerbal.text("Running TEST!")
speed = 0
delta = 0
run_time = -1
while run_time < simulation_lenght:
    last_speed = speed
    speed = car.speed()
    delta = speed - last_speed
    run_time += 1
    time.sleep(sleep_time)
    change = car.set_speed(target_speed)
    actual_speed_line.add_value(run_time, car.speed())
    change_line.add_value(run_time, change)
    actual_delta_line.add_value(run_time, delta)

car.stop()
kerbal.text("TEST Completed!")
window.render()
logging.info("Simulation completed!")
