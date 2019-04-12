class DummyStorage():

    def __init__(self,default=0):
        self.storage = {}
        self.default = default

    def save(self, key, value):
        self.storage[key] = value
        return self.storage

    def load(self, key):
        for el in self.storage:
            el +=1
            if key in self.storage:
                self.default = 1
                print(key,' = True')
                print(self.storage)
            else:
                self.default = 0
                print("new: ",key)

