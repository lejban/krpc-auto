import logging
import simple_pid


class SimpleCar:
    def __init__(self):
        self.throttle = 0
        self.brakes = 1
        self.pid = simple_pid.PID(1, 0.1, 0.05, setpoint=1)
        self.pid.output_limits = (-1, 1)

    def set_speed(self, target_speed):
        self.pid.setpoint = target_speed
        speed = self.speed()
        change = self.pid(speed)
        logging.info("Speed " + format(speed, '.4f') + " m/s, change: " + format(change, '.4f'))
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
