import time

def flying_time(start_time, suite_flag):
    if suite_flag == 1 and start_time is not None:
        elapsed_time = time.time() - start_time
        return elapsed_time