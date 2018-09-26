class SimpleCar:
    def __init__(self):
        self.throttle = 0
        self.brakes = 1

    def set_speed(self, target_speed):
        speed = self.speed()
        if speed > target_speed:
            self.brake()
            return -1
        elif speed < target_speed:
            self.accelerate(1)
            return 1
        else:
            return 0

    def accelerate(self, throttle):
        pass

    def brake(self, brake=True):
        pass

    def speed(self):
        pass

    def get_brakes(self):
        return self.brakes
