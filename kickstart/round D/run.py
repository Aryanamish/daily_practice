import os


class read_input:
    counter = 0
    inputs = [] 
    file_exist = True
    filepath = os.path.dirname(__file__) + "\\" + 'input'

    def __init__(self):
        if os.path.isfile(self.filepath):
            with open(self.filepath, 'r') as f:
                self.inputs = f.readlines()
        else:
            self.file_exist = False
            
    def input(self, string):
        if self.file_exist is True:
            if len(self.inputs)-1 >= self.counter:
                rv = self.inputs[self.counter]
                self.counter = self.counter + 1
                return rv
        else:
            return input(string)

