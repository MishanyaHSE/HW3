

from train import Train
from plane import Plane
from ship import Ship

def check_keys(data, container):
    checked_data = []
    for index, line in enumerate(data):
        if 1 <= line[0] <= 3 and index < container.MAX_LENGTH:
            checked_data.append(line)
        else:
            print(f"key error in line #{index} - '{line}'")
            break
    
    return checked_data


def build_container(container, line):
    transport_parameters = check_keys([list(map(int, item.split())) for item in line.split('\n')], container)
    transport_types = [Plane, Train, Ship]
    for line in transport_parameters:
        container.storage.append(transport_types[line[0] - 1]().read_transport_parameters(*line[1:]))
    return len(transport_parameters)