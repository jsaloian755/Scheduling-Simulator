
# this class will implement a FCFS scheduling policy for testing
class FCFS_Sched:
    # method to select process using the FCFS algorithm
    def select_proc(self, ready_queue):
        # check that there are processes ready to run
        if len(ready_queue) == 0:
            return None
        
        # return the first process in ready queue
        return ready_queue[0]



