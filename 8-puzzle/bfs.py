import board
import queue
import time


class Bfs:

    start_time = time.time()

    def __init__(self, board):
        self.board = board


    def goalTest(self, state, goalState=[0,1,2,3,4,5,6,7,8]):
        count = 0
        for number in goalState:
            if number == state[count]:
                return(True)
            else:
                return(False)
        count += 1

    def testQueue(self):
        frontier = queue.Queue([self.board])
        return("First Item: " + str(frontier.items))

    def bfs(self, goalState=[0,1,2,3,4,5,6,7,8]):

        frontier = queue.Queue([self.board])
        print("Frontier: " + str(frontier.items))
        explored = set([])
        frontier.enqueue([self.board])
        state = frontier.items[1]

        if self.goalTest(state):
            return(explored)

        oneBoard = board.Board(frontier.items[1])
        frontier2 = set([])
        for lyst in frontier.items:
            if frontier.items.index(lyst) != 0:
                frontier2.add(tuple(lyst))
        print("Tuple Frontier: " + str(frontier2))
        union = explored.union(frontier2)
        frontier.dequeue(frontier.items.index(frontier.items[0]))

        print("Frontier: After Dequeue" + str(frontier.items))
        print("Union: " + str(union))
        print("Board: " + str(self.board))
        print("Frontier: " + str(frontier.items))
        print("Explored: " + str(explored))

        #for neighbor in oneBoard.neighbors():
        #    if tuple(neighbor) not in union:
        #        explored.add(tuple(neighbor))
        #        frontier.enqueue(neighbor)

    #def path_to_goal(self,explored_nodes):
        ####path_lyst = []
        ###the sequence of moves taken to reach the goal
    def cost_of_path(self, explored_nodes):
        exp = path_to_goal(explored_nodes)
        return(len(explored_nodes))
    #the number of moves taken to reach the goal

    def nodes_expanded(self, explored_nodes):
        return(len(explored_nodes))
    #the number of nodes that have been expanded

    def search_depth(self, explored_nodes):
    #the depth within the search tree when the goal node is found
        return(cost_of_path(explored_nodes))


    #def max_search_depth(self, explored_nodes):
    #the maximum depth of the search tree in the lifetime of the algorithm
    ###maybe we can solve this by checking whether or not we get repeated
    ###states while searching, how deep can we go without repeating.


    def running_time(self, search_instance):
    #the total running time of the search instance, reported in seconds
        return(time.time() - start_time)

    def max_ram_usage():
        return(None)
    #the maximum RAM usage in the lifetime of the process as measured by the ru_maxrss attribute in the resource module, reported in megabytes
    ###????

lyst= [1,2,5,3,4,0,6,7,8]
search = Bfs(lyst)
print("The search starts here....")
print(search.bfs())
