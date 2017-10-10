class Queue:
    def __init__(self, list_of_lists):
        self.items = list_of_lists

    def isEmpty(self):
        return(self.items) == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self, number):
        self.items.pop(number)

    def size(self):
        len(self.items)

oneQueue = Queue([[1,2,3]])
print("Items: " + str(oneQueue.items))
oneQueue.enqueue([3,4,5])
print("Items: " + str(oneQueue.items))
print("First List: " + str(oneQueue.items[0]))
