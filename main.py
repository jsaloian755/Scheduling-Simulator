from simulator.process import Process
from simulator.sim import Simulator


# main method to create processes and test scheduling metrics
if __name__ == "__main__":
    # create processes
    processes = [Process("P1", 0, 5), Process("P2", 2, 3), Process("P3", 4, 2)]

    # create simulator and run processes
    sim = Simulator(processes)
    sim.run()

    # output performance metrics of scheduling algorithm
    sim.print_metrics()



