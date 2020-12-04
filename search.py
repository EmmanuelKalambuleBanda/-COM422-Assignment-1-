# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # node ← a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
    # create a node object with state and pathcost
    node = {
        'state': problem.getStartState(),
        'pathCost': 0
        }

    #if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
    #if a goal has been reached return a list of actions,
    if problem.isGoalState(node['state']):
        return[] #since we are starting out, no need to take any actions

    # frontier ← a LIFO Stack with node as the only element
    #Create a Stack to hold states
    frontier =  util.Stack() 
    frontier.push(node) #node is the only element
    # explored ← an empty set
    explored = set()
    # loop do

    while True:
        # if EMPTY?( frontier) then return failure
        if frontier.isEmpty():
            raise Exception ('Search Failed')
        # node ← POP( frontier) /* chooses the shallowest node in frontier */
        node = frontier.pop()
        # add node.STATE to explored
        explored.add(node['state'])
        # for each action in problem.ACTIONS(node.STATE) do
        #look for children who are successors
        successors = problem.getSuccessors(node['state'])
        for successor in successors: 
            # child ← CHILD-NODE(problem, node, action)
            #Create a child node based on the information we get from a successor which are state, action, cost
            child={ 'state': successor[0],
                    'action': successor[1],
                    'pathCost':  successor[2],
                    'parent': node # a parent of a child
                 }
                # if child.STATE is not in explored or frontier then
            if child['state'] not in explored:
                # if problem.GOAL-TEST(child.STATE) then return SOLUTION(child)
                #Checking the goal state
                if problem.isGoalState(child['state']):
                    actions = []
                    node = child
                    while 'parent' in node:
                        actions.append(node['action']) #this gives a reverse order path 
                        node = node['parent']
                    actions.reverse() #reverse the the order in the above line
                    return actions
                else:
                    # frontier ← INSERT(child, frontier)
                    frontier.push(child)

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #[Pseudocode For this Part was taken From Artificial Intelligence A Modern Approach Third Edition Stuart J. Russell and Peter Norvig Page.82]
    # function breadthFirstSearch(problem) returns a solution, or failure
    # node ← a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
    # create a node object with state and pathcost
    node = {
        'state': problem.getStartState(),
        'pathCost': 0
        }

    #if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
    #if a goal has been reached return a list of actions,
    if problem.isGoalState(node['state']):
        return[] #since we are starting out, no need to take any actions

    # frontier ← a FIFO queue with node as the only element
    #Create a Queue to hold states
    frontier =  util.Queue() 
    frontier.push(node) #node is the only element
    # explored ← an empty set
    explored = set()
    # loop do

    while True:
        # if EMPTY?( frontier) then return failure
        if frontier.isEmpty():
            raise Exception ('Search Failed')
        # node ← POP( frontier) /* chooses the shallowest node in frontier */
        node = frontier.pop()
        # add node.STATE to explored
        explored.add(node['state'])
        # for each action in problem.ACTIONS(node.STATE) do
        #look for children who are successors
        successors = problem.getSuccessors(node['state'])
        for successor in successors: 
            # child ← CHILD-NODE(problem, node, action)
            #Create a child node based on the information we get from a successor which are state, action, cost
            child={ 'state': successor[0],
                    'action': successor[1],
                    'pathCost':  successor[2],
                    'parent': node # a parent of a child
                 }
                # if child.STATE is not in explored or frontier then
            if child['state'] not in explored:
                # if problem.GOAL-TEST(child.STATE) then return SOLUTION(child)
                #Checking the goal state
                if problem.isGoalState(child['state']):
                    actions = []
                    node = child
                    while 'parent' in node:
                        actions.append(node['action']) #this gives a reverse order path 
                        node = node['parent']
                    actions.reverse() #reverse the the order in the above line
                    return actions
                else:
                # frontier ← INSERT(child, frontier)
                    frontier.push(child)

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
