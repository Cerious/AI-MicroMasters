class State:
    def __init__(self):
        self.state = []

    end
   
    def swap(x,y):
        self.state[x], self.state[y] = self.state[y], self.state[x]

    self.neighbors =  []

### swapping rules
    if self.state.index(0) == 0:
        swap(0, 1)
        neighbors.append(self.state)
        swap(0, 3)
        neighbors.append(self.state)
    elif self.state.index(0) == 1:
        swap(1, 0)
        neighbors.append(self.state)
        swap(1, 4)
        neighbors.append(self.state)
        swap(1, 2)
        neighbors.append(self.state)
    elif self.state.index(0) == 2:
        swap(2, 1)
        neighbors.append(self.state)
        swap(2, 5)
        neighbors.append(self.state)
    elif self.state.index(0) == 3:
        swap(3, 0)
        neighbors.append(self.state)
        swap(3, 4)
        neighbors.append(self.state)
        swap(3, 6)
    elif self.state.index(0) == 5:
        swap(5, 2)
        neighbors.append(self.state)
        swap(5, 8)
        neighbors.append(self.state)
        swap(5, 4)
        neighbors.append(self.state)
    elif self.state.index(0) == 6:
        swap(6, 3)
        neighbors.append(self.state)
        swap(6, 7)
        neighbors.append(self.state)
    elif self.state.index(0) == 7:
        swap(7, 4)
        neighbors.append(self.state)
        swap(7, 6)
        neighbors.append(self.state)
        swap(7, 8)
        neighbors.append(self.state)
    elif self.state.index(0) == 8:
        swap(8, 5)
        neighbors.append(self.state)
        swap(8, 7)
        neighbors.append(self.state)


class Solver:
