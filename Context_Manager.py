class File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    # Enter method to open the connection
    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()

files = []
for _ in range(10000):
    with File('/Users/rajeshjakkula/Documents/Pycharm_Pythoncode/foo.txt', 'w') as infile:
        infile.write('foo')
        files.append(infile)

