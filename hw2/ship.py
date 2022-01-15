import transport
from random import randint
from enum import Enum
from transport_error import Displacement_error

class Ship_types(Enum):
    liner = 1 
    tugboat = 2
    tanker = 3


class Ship(transport.Transport):
    def __init__(self) -> None:
        super().__init__()
        self.displacement = None
        self.type = None
    
    def read_transport_parameters(self, *args):
        super().read_transport_parameters(*args)
        if args[2] > 0:
            self.displacement = args[2]
        else: 
            raise Displacement_error
        if 4 > args[3] > 0:
            self.type = Ship_types(args[3])
        else: 
            raise TypeError
        return self

    def generate_parameters(self):
        self.speed = randint(50, 100)
        self.distance = randint(500, 10000)
        self.displacement = randint(10, 100)
        self.type = Ship_types(randint(1, 3))
        return self
    
    def print(self):
        print(f"It's a {self.type.name}. Displacement = {self.displacement}. Perfect time = {self.get_perfect_time()}")

    def write(self, out_stream):
        out_stream.write(f"It's a {self.type.name}. Displacement = {self.displacement}. Perfect time = {self.get_perfect_time()}\n")
