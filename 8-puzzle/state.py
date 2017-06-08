class State:
####how to access instace variables within a class
    
    def __init__(self, arr):
        self.state = arr
        
        
    def swap(arr, x, y):
        arr[x], arr[y] = arr[y], arr[x]

    
    def neighbors(arr):
        neighbor = []
        if arr.index(0) == 0:
            swap(arr,0, 1)
            neighbor.append(arr)
            swap(arr,0, 3)
            neighbor.append(arr)
        elif arr.index(0) == 1:
            swap(arr, 1, 0)
            neighbor.append(arr)
            swap(arr, 1, 4)
            neighbor.append(arr)
            swap(arr, 1, 2)
            neighbor.append(arr)
        elif arr.index(0) == 2:
            swap(arr, 2, 1)
            neighbor.append(arr)
            swap(arr, 2, 5)
            neighbor.append(arr)
        elif arr.index(0) == 3:
            swap(arr, 3, 0)
            neighbor.append(arr)
            swap(arr, 3, 4)
            neighbor.append(arr)
            swap(arr, 3, 6)
        elif arr.index(0) == 5:
            swap(arr, 5, 2)
            neighbor.append(arr)
            swap(arr, 5, 8)
            neighbor.append(arr)
            swap(arr, 5, 4)
            neighbor.append(arr)
        elif arr.index(0) == 6:
            swap(arr, 6, 3)
            neighbor.append(arr)
            swap(arr, 6, 7)
            neighbor.append(arr)
        elif arr.index(0) == 7:
            swap(arr, 7, 4)
            neighbor.append(arr)
            swap(arr, 7, 6)
            neighbor.append(arr)
            swap(arr, 7, 8)
            neighbor.append(arr)
        elif arr.index(0) == 8:
            swap(arr, 8, 5)
            neighbor.append(arr)
            swap(arr, 8, 7)
            neighbor.append(arr)
    
        neighbor

        
    
### swapping rules
    



initial = State([1,2,5,3,4,0,6,7,8])
print(initial.state)
print(initial.neighbors(initial.state)
###class Solver:
