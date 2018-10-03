import time
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

    def findAccForSpeed(self, target_speed, sleep_time, hits_needed=20, accuracy=0.1):
        self.stop()
        acc_value = []
        while len(acc_value) < hits_needed:
            speed = self.speed()
            change = self.set_speed(target_speed)
            time.sleep(sleep_time)
            if abs(speed - target_speed) < accuracy:
                acc_value.append(change)
            else:
                acc_value.clear()
        self.stop()
        acc = sum(acc_value) / hits_needed
        logging.info("Acceleration to keep speed " + str(target_speed) + " m/s for Car is " + str(acc) + " m/s2")
        return sum(acc_value) / hits_needed

    def findMaxAcc(self, max_speed, sleep_time, hits_needed=5, accuracy=0.1):
        self.stop()
        acc_value = []
        last_speed = 0
        last_delta = 0
        while len(acc_value) < hits_needed:
            speed = self.speed()
            self.set_speed(max_speed)
            delta = abs(last_speed - speed)
            if speed > max_speed:
                self.stop()
            time.sleep(sleep_time)
            if speed > (max_speed - accuracy * 50) and abs(last_delta - delta) < accuracy:
                acc_value.append(delta)
            else:
                acc_value.clear()
            last_speed = speed
            last_delta = delta
        self.stop()
        max_acc = sum(acc_value) / hits_needed
        logging.info("Max Acceleration for Car is " + str(max_acc) + " m/s2")
        return sum(acc_value) / hits_needed

    def accelerate(self, throttle):
        pass

    def brake(self, brake=True):
        pass

    def speed(self):
        pass

    def get_brakes(self):
        return self.brakes
