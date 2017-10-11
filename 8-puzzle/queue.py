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
