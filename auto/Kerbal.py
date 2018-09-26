import SimpleCar


class Vessel:
    def __init__(self, connection):
        self.connection = connection
        self.vessel = connection.space_center.active_vessel
        self.reference_frame = self.vessel.orbit.body.reference_frame
        self.position = connection.add_stream(self.vessel.position, self.reference_frame)
        self.flight = connection.add_stream(self.vessel.flight, self.reference_frame)
        self.brake()

    def visualize(self, enable=True):
        if enable:
            self.connection.drawing.add_direction((0, 1, 0), self.vessel.surface_velocity_reference_frame)

    def accelerate(self, throttle):
        self.vessel.control.brakes = False
        self.vessel.control.wheel_throttle = throttle

    def brake(self, brake=True):
        self.vessel.control.wheel_throttle = 0
        self.vessel.control.brakes = brake

    def speed(self):
        return self.flight().speed


class Car(Vessel, SimpleCar.SimpleCar):
    def __init__(self, connection):
        SimpleCar.SimpleCar.__init__(self)
        Vessel.__init__(self, connection)
