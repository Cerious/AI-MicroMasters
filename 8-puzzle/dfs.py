import state
import bfs
from bfs import goalTest

class Dfs:
    start_time = time.time()
    
    def __init__(self, board):
        self.board = []

    def dfs(self,initialState, goalState = [0,1,2,3,4,5,6,7,8]):
        frontier = Stack()
        explored = {}

        while not frontier.isEmpty():
            frontier.pop(state)
            explored.add(state)


            if goalTest(state):
                return(success(state))

            for neighbor in state.neighbors():
                union = explored.add(frontier)
                if neighbor not in union:
                    frontier.push(state)

        #return(False)

    def path_to_goal(explored_nodes):
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
    #the depth within the search tree when the goal node is found

    def max_search_depth(explored_nodes):
    #the maximum depth of the search tree in the lifetime of the algorithm

    def running_time(search_instance):
    #the total running time of the search instance, reported in seconds

    def max_ram_usage():
    #the maximum RAM usage in the lifetime of the process as measured by the ru_maxrss attribute in the resource module, reported in megabytes
    ###????
