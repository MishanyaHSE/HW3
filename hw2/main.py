import sys
import time

from container import Container
from build_container import build_container
from plane import Plane
from train import Train
from ship import Ship
from random import choice

if __name__ == '__main__':
    start_time = time.time()
    print("Start")

    if len(sys.argv) != 5:
        if sys.argv[1] == '-n':
            print("Incorrect command line! You must write: python main -n \"number\" <outputFileName1> <outputFileName2>")
        elif sys.argv[1] == '-f':
            print("Incorrect command line! You must write: python main -f <inputFileName> <outputFileName1> <outputFileName2>")
        else:
            print("Incorrect command line!")
    
    cont = Container()

    if sys.argv[1] == '-f':
        input_file= sys.argv[2]
        output_file1 = sys.argv[3]
        output_file2 = sys.argv[4]

        input_stream = open(input_file)
        input_string = input_stream.read()
        input_stream.close()

        transport_count = build_container(cont, input_string)
        if not transport_count:
            print('You have no transport')

    elif sys.argv[1] == '-n':
        size = int(sys.argv[2])
        output_file1 = sys.argv[3]
        output_file2 = sys.argv[4]

        if size > Container.MAX_LENGTH or size <= 0:
            print(f"Incorrect number of figures = {size}. Set 0 < number <= {cont.MAX_LENGTH}")
            exit()
        
        for i in range(size):
            cont.storage.append(choice([Plane, Train, Ship])().generate_parameters())

    else:
        print('Specify correct mode flag (-f or -n)')
    
    print("The container stores", len(cont.storage), "transports:")
    cont.print()

    output_stream1 = open(output_file1, 'w+')
    output_stream1.write(f"The container stores {len(cont.storage)} transports:\n")
    cont.write(output_stream1)
    output_stream1.close()

    avg_time = cont.sort_by_perfect_time()

    print("\nThe container after sorting:")
    cont.print()

    output_stream2 = open(output_file2, 'w+')
    output_stream2.write("The container after sorting elements:\n")
    cont.write(output_stream2)
    output_stream2.write(f"Average time is {avg_time}")
    output_stream2.close()

    print("\n%s seconds" % (time.time() - start_time))

    print("Finish")