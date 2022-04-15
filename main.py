import os
from __datatype___ import *

class TXT:
    def __init__(self, path_=None):
        self.cwd = os.getcwd()
        if path_:
            
            self.binary = self.binaries(path_)
            self.size = None
            self.bytes = None
            self.asciiValues = None
            self.dataType = self.dataType(path_)


    def dataType(self, file=str):
        class FTDT:
            def __init__(self):
                self.value = None
                self.cwd = os.getcwd()
                self.dataType = None
                self.restore = """def data():
        return [type({}), {}]"""

            def analyzeFileText(self, path_=str):

                if path_:
                    path = os.path.join(self.cwd, path_)
                    with open(path, 'r') as f:
                        self.read = f.read()
                    with open('__datatype___.py', 'w') as py:
                        py.write(self.restore.format(self.read, self.read))
                        self.value = data()[1]
                return data()[0]

        ftdt = FTDT()
        analyze = ftdt.analyzeFileText(file)
        if analyze:
            print(ftdt.value)
            return analyze

    def dump(self, object=None, file=str):
        path = os.path.join(self.cwd, file)
        with open(path, 'w') as f:
            dump = f.write(str(object))
            return dump

    def load(self, file=str):
        path = os.path.join(self.cwd, file)
        with open(path, 'r') as f:
            load = f.read()
            return load

    def binaries(self, file=str):
        with open(file, 'r') as f:
            read = f.read()
            binary = ' '.join(format(ord(c), 'b') for c in read)
            return binary
