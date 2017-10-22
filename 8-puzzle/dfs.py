import board
import stack
import time


class Dfs:
    start_time = time.time()

    def __init__(self, board):
        self.board = board


    def goalTest(self, state, goalState=[0,1,2,3,4,5,6,7,8]):

        if state == goalState:
            return(True)
        else:
            return(False)

    def dfs(self, goalState = [0,1,2,3,4,5,6,7,8]):
        state = self.board
        frontier = stack.Stack([state])
        explored = set([])
        count = 0
        while self.goalTest(frontier.items[0]) == False:

            oneBoard = board.Board(frontier.items[0])
            frontier2 = set([])

            for lyst in frontier.items:
                frontier2.add(tuple(lyst))

            #print("Frontier 2: " + str(frontier2))

            frontier.pop()

            union = explored.union(frontier2)
            #print("Board: " + str(oneBoard))
            #print("Board Neighbors:" + str(oneBoard.neighbors()))
            for neighbor in oneBoard.neighbors():
                if tuple(neighbor) not in union:
                    explored.add(tuple(neighbor))
                    frontier.push(neighbor)

            print("Iteration Number: " + str(count+1))
            #print(str(frontier.items[0]))
            #print(self.goalTest(frontier.items[0]))
            count += 1
            print("#################################################")

        #return(False)

    #def path_to_goal(explored_nodes):
        ####path_lyst = []
    #the sequence of moves taken to reach the goal

    def cost_of_path(explored_nodes):
        exp = path_to_goal(explored_nodes)
        return(len(explored_nodes))
    #the number of moves taken to reach the goal

    def nodes_expanded(explored_nodes):
        return(len(explored_nodes))
    #the number of nodes that have been expanded

    def search_depth(explored_nodes):
        return(None)
    #the depth within the search tree when the goal node is found

    def max_search_depth(explored_nodes):
        return(None)
    #the maximum depth of the search tree in the lifetime of the algorithm

    def running_time(search_instance):
        return(None)
    #the total running time of the search instance, reported in seconds

    def max_ram_usage():
        return(None)
    #the maximum RAM usage in the lifetime of the process as measured by the ru_maxrss attribute in the resource module, reported in megabytes
    ###????
lyst = [1,2,5,3,4,0,6,7,8]
search = Dfs(lyst)

print("The search starts here....")
print(search.dfs())
