print('Hello world =')
class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h
class DeskTable(Table):
    def square(self):
        return self.length*self.width
class ComputerTable(DeskTable):
    def square(self, monitor = 0.0):
        return self.length*self.width - monitor
t1 = Table(15, 18, 75)
t2 = DeskTable(0.8, 0.6, 0.7)
t3 = ComputerTable(0.8, 0.6, 0.7)
print(t2.square())
print(t3.square(0.3))