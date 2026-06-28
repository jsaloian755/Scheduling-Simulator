

# class defining the simulator that will run various scheduling algorithms
# see 'Week 5 Notes' for more details
class Simulator:
    #
    def __init__(self, procs, sched):
        # create fields to describe the simulator
        self.time = 0
        self.procs = procs

        self.ready_queue = []
        self.compl_procs = []

        self.sched = sched

    # check for any newly arrived processes and add to ready queue
    def add_arriving_proc(self):
        # iterate through all processes
        for p in self.procs:
            # if just arrived then add to ready queue
            if p.arrival_time == self.time:
                self.ready_queue.append(p)
    
    # helper to just choose first process (will later be replaced by sched algorithms)
    def select_proc(self):
        # check that there are ready processes
        if len(self.ready_queue) == 0:
            return None
        
        # return first process in ready queue
        return self.ready_queue[0]

    # helper to execute a single time step for a given process
    def exec_proc(self, proc):
        # set start time if necessary
        if proc.start_time is None:
            proc.start_time = self.time
        
        # decrease remaining runtime for process by 1
        proc.rem_time -= 1

        # if process is complete then record completion time and update data structures
        if proc.rem_time <= 0:
            # record completion time
            proc.compl_time = self.time + 1

            # remove finished process from ready queue
            self.ready_queue.remove(proc)

            # add finished process to the list of completed processes
            self.compl_procs.append(proc)
    
    # main sim loop
    def run(self):
        # check that there are still processes needing to run
        while len(self.compl_procs) < len(self.procs):
            # add process to ready queue
            self.add_arriving_proc()

            # select process to run according to given scheduling policy
            proc = self.sched.select_proc(self.ready_queue)

            # execute the selected process
            if proc is not None:
                self.exec_proc(proc)

            # increment simulation clock
            self.time += 1


    # get turnaround time performance metric
    def turnaround_time(self, proc):
        # completion time - arrival time
        return (proc.compl_time - proc.arrival_time)

    # get response time performance metric
    def response_time(self, proc):
        # start time - arrival time
        return (proc.start_time - proc.arrival_time)

    # get wait time performance metric
    def wait_time(self, proc):
        # turnaround time - burst time
        return (self.turnaround_time(proc) - proc.burst_time)
    
    # get throughput performance metric
    def throughput(self):
        # number of completed processes / total simulation time
        return (len(self.compl_procs) / self.time)
    
    
    # helper method to print out performance metrics
    def print_metrics(self):
        # declare variables to hold performance metrics
        total_wait = 0
        total_turnaround = 0
        total_response = 0

        # iterate through finished processes
        for proc in self.compl_procs:
            # accumulate performance metrics for process
            total_wait += self.wait_time(proc)
            total_turnaround += self.turnaround_time(proc)
            total_response += self.response_time(proc)

        # get number of processes completed
        count = len(self.compl_procs)

        # output results
        print("\nSimulation Results")

        print("Average Waiting Time:", total_wait / count)
        print("Average Turnaround Time:", total_turnaround / count)
        print("Average Response Time:", total_response / count)
        print("Throughput:", self.throughput())


