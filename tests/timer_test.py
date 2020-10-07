import signal
import threading
import time
from datetime import timedelta

WAIT_TIME_SECONDS = 60


class ProgramKilled(Exception):
    pass


def foo():
    print(time.ctime())


def signal_handler(signum, frame):
    raise ProgramKilled


class Job(threading.Thread):
    def __init__(self, interval, execute, *args, **kwargs):
        threading.Thread.__init__(self)
        self.daemon = False
        self.stopped = threading.Event()
        self.interval = interval
        self.execute = execute
        self.args = args
        self.kwargs = kwargs

    def stop(self):
        self.stopped.set()
        self.join()

    def run(self):
        while not self.stopped.wait(self.interval.total_seconds()):
            self.execute(*self.args, **self.kwargs)


if __name__ == "__main__":
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    print(time.ctime())
    job = Job(interval=timedelta(seconds=WAIT_TIME_SECONDS), execute=foo)
    job.start()

    while True:
        try:
            time.sleep(WAIT_TIME_SECONDS)
        except ProgramKilled:
            print("Program killed")
            job.stop()
            break
# output
# Tue Oct 16 17:47:51 2018
# Tue Oct 16 17:47:52 2018
# Tue Oct 16 17:47:53 2018
# Program killed
