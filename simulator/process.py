
# this class defines a process with the necessary attributes
# see 'Week 5 Notes' for more details
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        # create fields to describe a process
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.start_time = None
        self.rem_time = burst_time
        self.compl_time = None

