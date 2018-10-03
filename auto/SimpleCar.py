import logging
import simple_pid


class SimpleCar:
    def __init__(self, pid_start_values):
        self.throttle = 0
        self.brakes = 1
        self.pid_start_values = pid_start_values
        p, i, d, limits = pid_start_values
        self.pid = simple_pid.PID(p, i, d, setpoint=0)
        self.pid.output_limits = limits

    def set_speed(self, target_speed):
        speed = self.speed()
        self.pid.setpoint = target_speed
        change = self.pid(speed)
        logging.debug("Speed " + format(speed, '.4f') + " m/s, change: " + format(change, '.4f'))
        self.accelerate(change)
        return change

    def accelerate(self, throttle):
        pass

    def brake(self, brake=True):
        pass

    def speed(self):
        pass

    def get_brakes(self):
        return self.brakes
