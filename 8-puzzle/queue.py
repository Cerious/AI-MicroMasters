class Queue:
    def __init__(self, list_of_lists):
        self.items = list_of_lists

    def isEmpty(self):
        return(self.items) == []

    def enqueue(self, position,item):
        self.items.insert(position, item)

    def dequeue(self, number):
        self.items.pop(number)

    def size(self):
        len(self.items)
