class Board:
####how to access instace variables within a class

    def __init__(self, arr):
        self.state = arr


    def swap(self,arr,x,y):
        arr1 = list(arr)
        arr1[x], arr1[y] = arr1[y], arr1[x]
        return(arr1)


    def neighbors(self):
        neighbor = []
        stt1 = list(self.state)
        stt2 = list(self.state)
        stt3 = list(self.state)
        stt4 = list(self.state)
        ###swpping rules.
        if self.state.index(0) == 0:
            stt1 = self.swap(stt1,0,1)
            neighbor.append(stt1)
            stt2 = self.swap(stt2,0,3)
            neighbor.append(stt2)
        elif self.state.index(0) == 1:
            stt1 = self.swap(stt1,1,0)
            neighbor.append(stt1)
            stt2 = self.swap(stt2,1,4)
            neighbor.append(stt2)
            stt3 = self.swap(stt3,1,2)
            neighbor.append(stt3)
        elif self.state.index(0) == 2:
            stt1 = self.swap(stt1,2,1)
            neighbor.append(stt1)
            stt2 = self.swap(stt2,2,5)
            neighbor.append(stt2)
            ###below is broken
        elif self.state.index(0) == 3:
            stt1 = self.swap(stt1,3,0)
            neighbor.append(stt1)
            stt2 = self.swap(stt2,3,4)
            neighbor.append(stt2)
            stt3 = self.swap(stt3,3,6)
            neighbor.append(stt3)
        elif self.state.index(0) == 4:
            stt1 = self.swap(stt1,4,1)
            neighbor.append(stt1)
            stt2 = self.swap(stt2,4,3)
            neighbor.append(stt2)
            stt3 = self.swap(stt3,4,7)
            neighbor.append(stt3)
            stt4 = self.swap(stt4,4,5)
            neighbor.append(stt4)
        elif self.state.index(0) == 5:
            stt1 = self.swap(stt1,5,2)
            neighbor.append(stt1)
            stt2 = self.swap(stt2,5,8)
            neighbor.append(stt2)
            stt3 = self.swap(stt3,5,4)
            neighbor.append(stt3)
        elif self.state.index(0) == 6:
            stt1 = self.swap(stt1,6,3)
            neighbor.append(stt1)
            stt2 = self.swap(stt2,6,7)
            neighbor.append(stt2)
        elif self.state.index(0) == 7:
            stt1 = self.swap(stt1,7,4)
            neighbor.append(stt1)
            stt2 = self.swap(stt2,7,6)
            neighbor.append(stt2)
            stt3 = self.swap(stt3,7,8)
            neighbor.append(stt3)
        elif self.state.index(0) == 8:
            stt1 = self.swap(stt1,8,5)
            neighbor.append(stt1)
            stt2 = self.swap(stt2,8,7)
            neighbor.append(stt2)
        #print(self.swap(0, 1))
        #print(stt1 == stt2)
        return(neighbor)
        return(neighbor)



### swapping rules



#lyst = [7,2,5,3,4,0,1,6,8]
#initial = Board(lyst)
#print("State: " + str(initial.state))
#print(initial.swap(0,1))
#print(initial.neighbors())
###class Solver:
