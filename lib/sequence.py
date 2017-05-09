import time


class Sequence(object):
    def __init__(self, generator):
        self.generator = generator
        print("sequence init")

    def __iter__(self):
        return self.generator()

    def display(self):
        for frame in self.generator():
            print("display sequence frame", frame)
            time.sleep(0.1)

        return self

    def next_frame(self):
        pass
