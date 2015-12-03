import sys
import time


class ProgressClock(object):
    """Simple progress class showing a turning bar /-\|."""
    def __init__(self, message, fp=sys.stderr):
        self.fp = fp
        self.fp.write(message + ' |')
        self.counter = 0

    def tick(self):
        if self.counter == 0:
            self.fp.write('\b/')
        elif self.counter == 1:
            self.fp.write('\b-')
        elif self.counter == 2:
            self.fp.write('\b\\')
        else:
            self.fp.write('\b|')
        self.counter = (self.counter + 1) % 4

    def end(self):
        self.fp.write('\b \n')

    def test(self):
        p = ProgressClock("loading...")
        for i in range(10):
            p.tick()
            time.sleep(.5)
        p.end()
