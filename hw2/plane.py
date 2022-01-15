import transport
from random import randint, choice

class Plane(transport.Transport):
    def __init__(self) -> None:
        super().__init__()
        self.range = None
        self.capacity = None
    
    def read_transport_parameters(self, *args):
        super().read_transport_parameters(*args)
        self.range = args[2]
        self.capacity = args[3]
        return self

    def generate_parameters(self):
        self.speed = randint(300, 1200)
        self.distance = randint(500, 2000)
        self.range = randint(100, 1000)
        self.capacity = randint(50, 400)
        return self
    
    def print(self):
        print(f"It's a Plane. Range = {self.range}. Capacity = {self.capacity} Perfect time = {self.get_perfect_time()}")

    def write(self, out_stream):
        out_stream.write(f"It's a Plane. Range = {self.range}. Capacity = {self.capacity} Perfect time = {self.get_perfect_time()}\n")
