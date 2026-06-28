from simulator.process import Process
from simulator.sim import Simulator

# scheduler imports
from schedulers.fcfs import FCFS_Sched
from schedulers.sjf import SJF_Sched
from schedulers.rr import RR_Sched


# main method to create processes and test scheduling metrics
if __name__ == "__main__":
    # create processes
    processes = [Process("P1", 0, 5), Process("P2", 2, 3), Process("P3", 4, 2)]

    # choose a scheduler for testing
    sched = FCFS_Sched()

    # create simulator and run processes
    sim = Simulator(processes, sched)
    sim.run()

    # output performance metrics of scheduling algorithm
    sim.print_metrics()



