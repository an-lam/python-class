import sqlite3
from datetime import datetime, timedelta
import time
#import Schedule
from Schedule import Schedule

if __name__ == '__main__':
    sched = Schedule()
    testcases = ["tc1", "tc2", "tc3"]
    for tc in testcases:
        futuredate = datetime.now() + timedelta(seconds=15)
        sched.add_test(tc, futuredate)

    #while (True):
    cont = input("Do you want to continue?")
    while (cont == "y" or cont == "Y"):
        task_list = sched.show_schedule()
        #print(task_list)
        # Check to see if it's time to run
        for task in task_list:
            tc, starttime = task
            # This is true only after 4 loop iterations
            if starttime < str(datetime.now()):
                print("Time to run test case: {}, time: {}".format(tc, starttime))

        time.sleep(5)
        cont = input("Do you want to continue?")

    sched.cleanup()
