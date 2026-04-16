class queue:
    def __init__(self, size):
        self.size = size
        self.container = []

    def push(self, ele):
        if len(self.container) == self.size:
            print("Full")
            return
        self.container.append(ele)

    def pop(self):
        if len(self.container) == 0:
            print("Empty")
            return None
        return self.container.pop(0)  

    def show(self):
        if len(self.container) == 0:
            print("Empty")
            return
        print(self.container)


class stack:
    def __init__(self, size):
        self.size = size
        self.container = []

    def push(self, ele):
        if len(self.container) == self.size:
            print("Full")
            return
        self.container.append(ele)

    def pop(self):
        if len(self.container) == 0:
            print("Empty")
            return None
        return self.container.pop()  

    def show(self):
        if len(self.container) == 0:
            print("Empty")
            return
        print(self.container)
