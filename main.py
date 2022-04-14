import os
from __datatype___ import *

def dataType(path=str):
    class FTDT:
        def __init__(self, path_=None):
            self.value = None
            self.path_ = path_
            self.cwd = os.getcwd()
            self.dataType = None
            self.restore = """def data():
    return [type({}), {}]"""


            if path_:
                self.path = os.path.join(self.cwd, path_)
                with open(self.path, 'r') as f:
                    self.read = f.read()


        def analyzeFileText(self, path_=str):
            if self.path_:
                with open(self.path, 'r') as f:
                    self.read = f.read()

            if path_:
                path = os.path.join(self.cwd, path_)
                with open(path, 'r') as f:
                    self.read = f.read()
                with open('__datatype___.py', 'w') as py:
                    py.write(self.restore.format(self.read, self.read))
                    self.value = data()[1]
            return data()[0]

    ftdt = FTDT()
    analyze = ftdt.analyzeFileText(path)
    if analyze:
        print(ftdt.value)
        return analyze
