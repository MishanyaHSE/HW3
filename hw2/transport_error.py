class Transport_error(Exception):
    pass
    
class Incorrect_transport_speed(Transport_error):
    def __init__(self, speed):
        self.speed = speed
    def __str__(self) -> str:
        return f'speed error - {self.speed} - is less or equals to zero'

class Incorrect_transport_distance(Transport_error):
    def __init__(self, distance):
        self.distance = distance
    def __str__(self) -> str:
        return f'distance error - {self.distance} - is less or equals to zero'

class Cart_number_error(Transport_error):
    def __str__(self) -> str:
        return 'Invalid cart number'

class Displacement_error(Transport_error):
    def __str__(self) -> str:
        return 'Invalid displacement'