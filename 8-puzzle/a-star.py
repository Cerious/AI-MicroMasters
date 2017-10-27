import state
import queue
import bfs
import heap

class Ast:

    start_time = time.time()

    def __init__(self, board):
        self.board = board

    #cost to reach node N
    def cost_to_N(currentNode, goalNode):
        return(None)

        
    def ast(initialState, goalTest):
        ###/*Cost*/f(n) = G(n) + h(n)
        ###inorder to calculte the cost we will first need to calculate the
        ###Manhattan dist. (i.e. sum of horz. & vert. dist.)

        frontier = Heap()
        explored = {}

        while not frontier.isEmpty():
            state = frontier.deleteMin()

            if goalTest(state):
                return(success(state))

        for neighbor in state.neighbors
            union = exploerd.add(frontier)
            if not neighbor in union:
                frontier.insert(state)
            else if neighbor in frontier:
                frontier.decreaseKey(neighbor)


    def path_to_goal(explored_nodes):
        ####path_lyst = []
    #the sequence of moves taken to reach the goal

    def cost_of_path(explored_nodes):
    #the number of moves taken to reach the goal
        exp = path_to_goal(explored_nodes)
        return(len(explored_nodes))

    def nodes_expanded(explored_nodes):
    #the number of nodes that have been expanded
        return(len(explored_nodes))

    def search_depth(explored_nodes):
    #the depth within the search tree when the goal node is found
        depth = len(path_to_goal(explored_nodes))
    def max_search_depth(explored_nodes):
    #the maximum depth of the search tree in the lifetime of the algorithm

    def running_time(search_instance):
    #the total running time of the search instance, reported in seconds
        return(time.time() - start_time)
    def max_ram_usage():
    #the maximum RAM usage in the lifetime of the process as measured by the ru_maxrss attribute in the resource module, reported in megabytes
    ###????
