import transport
from random import randint
from transport_error import Cart_number_error


class Train(transport.Transport):
    def __init__(self) -> None:
        super().__init__()
        self.cart_number = None
    
    def read_transport_parameters(self, *args):
        super().read_transport_parameters(*args)
        if args[2] >= 10:
            self.cart_number = args[2]
        else:
            raise Cart_number_error
        return self

    def generate_parameters(self):
        self.speed = randint(80, 300)
        self.distance = randint(100, 1500)
        self.cart_number = randint(10, 100)
        return self
    
    def print(self):
        print(f"It's a Train. Cart number = {self.cart_number}. Perfect time = {self.get_perfect_time()} ")

    def write(self, out_stream):
        out_stream.write(f"It's a Train. Cart number = {self.cart_number}. Perfect time = {self.get_perfect_time()}\n")
