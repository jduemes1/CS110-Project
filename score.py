class score:
    def __init__(self):
        self.count = 0
    def increase(self, k = False):
        if k:
            self.count+=10
        else:
            self.count+=1
        return self.count
