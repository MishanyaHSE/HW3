

class Container:
    MAX_LENGTH = 10000

    def __init__(self) -> None:
        self.storage = []
    
    def print(self):
        for index, transport  in enumerate(self.storage):
            print(str(index + 1) + '.', end=' ')
            transport.print()
    
    def write(self, out_stream):
        for index, transport  in enumerate(self.storage):
            out_stream.write(str(index+1) + '. ')
            transport.write(out_stream)
    
    def sort_by_perfect_time(self):
        avg_time = sum([transport.get_perfect_time() for transport in self.storage])/len(self.storage)
        self.storage = [t for t in self.storage if t.get_perfect_time() <= avg_time] + [t for t in self.storage if t.get_perfect_time() > avg_time]
        return avg_time