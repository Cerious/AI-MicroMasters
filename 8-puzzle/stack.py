class Stack:
     def __init__(self, list_of_lists):
         self.items = list_of_lists

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.insert(0, item)

     def pop(self):
         return self.items.pop(0)

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

newStack = Stack([[1,2,5,3,4,0,6,7,8]])
print(newStack.items)
print(newStack.push([1,2,5,3,0,6,4,7,8]))
print(newStack.items)
print("First Item................ ")
print(newStack.items[0])
print("Popped Item: ")
print(newStack.pop())
print("New List: ")
print(newStack.items)
