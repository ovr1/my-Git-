class DummyStorage():

    def __init__(self,default=0):
        self.storage = {}
        self.default = default

    def save(self, key, value):
        self.storage[key] = value
        return self.storage

    def load(self, key):
        try:
            for key in self.storage:
                if key in self.storage:
                    print(key,' = True')
                else:
                    print(key, ' = False')
        except:
            print(0)


