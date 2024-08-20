from math import sin, cos, radians


class Entity:
    def __init__(self, position, size, status):
        self.position = position
        self.size = size

        self.speed = status["speed"]

    def move(self, direction):
        self.position = (self.position[0] + cos(radians(direction)) * self.speed,
                         self.position[1] + sin(radians(direction)) * self.speed)
