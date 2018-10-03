import time
import krpc

import SimpleCar
import AICar

class Kerbal:
    def __init__(self):
        self.connection = krpc.connect()
        self.infobox = self.debugText()

    def text(self, text_str):
        self.infobox.content = text_str

    def reset(self):
        self.connection.space_center.quickload()
        self.camera = self.connection.space_center.camera
        self.camera.mode = self.camera.mode.chase
        time.sleep(2)
        self.camera.distance = 5
        time.sleep(1)
        self.camera.heading = 75
        self.infobox = self.debugText()


    def debugText(self):
        self.canvas = self.connection.ui.stock_canvas
        screen_size = self.canvas.rect_transform.size
        panel = self.canvas.add_panel()
        rect = panel.rect_transform
        rect.size = (screen_size[0] - 200, 30)
        rect.position = (0, screen_size[1]/2 - 110)
        text = panel.add_text("")
        text.rect_transform.size = rect.size
        text.rect_transform.position = (0, 0)
        text.color = (1, 1, 1)
        text.size = 18
        text.alignment = text.alignment.middle_center
        return text

class Vessel:
    def __init__(self, kerbal):
        self.connection = kerbal.connection
        self.vessel = self.connection.space_center.active_vessel
        self.reference_frame = self.vessel.orbit.body.reference_frame
        self.position = self.connection.add_stream(self.vessel.position, self.reference_frame)
        self.flight = self.connection.add_stream(self.vessel.flight, self.reference_frame)
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

    def stop(self, accuracy=0.01):
        self.brake()
        while self.speed() > accuracy:
            time.sleep(0.1)
            pass

    def speed(self):
        return self.flight().speed


class SimpleKerbalCar(Vessel, SimpleCar.SimpleCar):
    def __init__(self, connection, pid_start_values):
        Vessel.__init__(self, connection)
        SimpleCar.SimpleCar.__init__(self, pid_start_values)


class AIKerbalCar(Vessel, AICar.AICar):
    def __init__(self, kerbal):
        AICar.AICar.__init__(self)
        Vessel.__init__(self, kerbal)

