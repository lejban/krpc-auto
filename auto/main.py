import time
import logging
import krpc

import Kerbal
import Graph

pid_start_values = [1, 0.1, 0.1]


logging.basicConfig(format="%(message)s", level=logging.INFO)
target_speed = 5
connection = krpc.connect()
car = Kerbal.Car(connection, pid_start_values)
g_win = Graph.Window("Stats", "PID:" + str(pid_start_values))
g_speed = Graph.Graph("Speed", "m/s")
q_change = Graph.Graph("Change", "Speed delta")
g_win.add_graph(g_speed)
g_win.add_graph(q_change)

logging.info("Simulation Started!")
run_time = 0
while run_time < 60:
    run_time += 1
    time.sleep(0.1)
    change = car.set_speed(target_speed)
    g_speed.add_value(run_time, car.speed())
    q_change.add_value(run_time, change)

car.brake()
g_win.render()
logging.info("Simulation completed!")
