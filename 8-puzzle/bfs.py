import board
import queue
import time


class Bfs:

    start_time = time.time()

    def __init__(self, board):
        self.board = board


    def goalTest(self, state, goalState=[0,1,2,3,4,5,6,7,8]):

        if state == goalState:
            return(True)
        else:
            return(False)


    def bfs(self,goalState=[0,1,2,3,4,5,6,7,8]):
        arr = self.board
        frontier = queue.Queue([arr])
        explored = set([])
        count = 0
        while self.goalTest(frontier.items[0]) == False:

            oneBoard = board.Board(frontier.items[0])

            frontier2 = set([])

            par_nei = {}
            #make a dictionary where neighbors are keys and parents
            #are neighbors

            for lyst in frontier.items:
                #if frontier.items.index(lyst) != 0:
                frontier2.add(tuple(lyst))
            print("Frontier 2: " + str(frontier2))

            frontier.dequeue(frontier.items.index(frontier.items[0]))

            union = explored.union(frontier2)
            for neighbor in oneBoard.neighbors():
                if tuple(neighbor) not in union:
                    explored.add(tuple(neighbor))
                    frontier.enqueue(len(frontier.items), neighbor)

            if self.goalTest(frontier.items[0]):
                print("Success...")
                return(explored)

            print("Iteration Number: " + str(count+1))
            print(str(frontier.items[0]))
            print(self.goalTest(frontier.items[0]))

            print("#################################################")
            count += 1




    #def path_to_goal(self,explored_nodes):
        ####path_lyst = []
        ###the sequence of moves taken to reach the goal
        #sett = []
        #for item in explored:
        #    newSquare = board.Board(item)
        #    state = newSquare.neighbors()

        #    print("Item outer epoch: " + str(item))

            #print("xxx: neigh" + str(state))
        #    for q in explored:

        #        print("Q: " + str(q))
        #        print("State: " + str(state))
        #        print("State inckudes q?" + str(list(q) in state))
        #        if list(q) in state:
        #            sett.append(list(q))
        #    print(sett)


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
        start_time = time.time()
        search_instance
        return(str(time.time() - start_time) + " seconds...")

    def max_ram_usage():
        return(None)
    #the maximum RAM usage in the lifetime of the process as measured by the ru_maxrss attribute in the resource module, reported in megabytes
    ###????

lyst= [1,2,5,3,4,0,6,7,8]
search = Bfs(lyst)
print("The search starts here....")
#print(search.board)
print(search.bfs())
print(search.running_time(search.bfs))
