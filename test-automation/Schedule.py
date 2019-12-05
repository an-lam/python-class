import sqlite3
from datetime import datetime, timedelta

class Schedule:

    @staticmethod
    def _cur_time():
        return str(datetime.now())

    #def __init__(self, tcname: str, time):
    def __init__(self):
        # Create a connection object
        self.db = sqlite3.connect("testschedule.sqlite")
        self.db.execute("CREATE TABLE IF NOT EXISTS schedule (tcname TEXT NOT NULL, "
                   " starttime TIMESTAMP NOT NULL, PRIMARY KEY (starttime, tcname))")

    def add_test(self, tcname: str, time):
        self.db.execute("INSERT INTO schedule VALUES(?, ?)", (tcname, time))
        self.db.commit()

    def show_schedule(self):
        task_list = []
        for row in self.db.execute("SELECT * FROM schedule"):
            tcname, starttime = row
            task_list.append(row)
            print("testcase: {}, starttime: {}".format(tcname, starttime))

        return task_list

    def cleanup(self):
        self.db.execute("DROP TABLE IF EXISTS schedule")
        self.db.close()

if __name__ == "__main__":
    sched = Schedule()
    sched.add_test("tc1", datetime.now())
    sched.add_test("tc2", datetime.now() + timedelta(days=1))

    sched.show_schedule()

    sched.cleanup()