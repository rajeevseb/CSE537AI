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


    stack = util.Stack()
    stack .push(problem.getStartState())
    currentState =  stack.pop();


    print problem
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    stack = util.Stack()
    directionStack =util.Stack()
    startState = problem.getStartState();

    explored= set();
    augmentedStartState = (startState,'START',0)
    stack.push(augmentedStartState);

    Directiondict = {}

    while(stack.isEmpty()== False):
        currentState = stack.pop();
        if (problem.isGoalState(currentState[0])) :
            directions =util.Stack();
            directions.push(currentState[1])
            current = currentState
            while(current != augmentedStartState):
                directions.push(Directiondict[current][1]);
                current = Directiondict[current];
            directions.list.reverse()
            print(' '.join(directions.list[1:]));
            return ( directions.list[1:])
        else:
            expanded = problem.getSuccessors(currentState[0]);
            explored.add(currentState[0]);
            for node in expanded :
                if(node[0] not in explored):
                     stack.push(node)
                     Directiondict[node] = currentState




    return "PATH NOT FOUND"




    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    queue = util.Queue()
    startState = problem.getStartState();

    explored = [];
    augmentedStartState = (startState, [])
    queue.push(augmentedStartState);

    while (queue.isEmpty() == False):
        currentState = queue.pop();
        if (problem.isGoalState(currentState[0])):
            return currentState[1]
        else:
            expanded = problem.getSuccessors(currentState[0]);
            explored.append(currentState[0]);
            pathTillCurrent = currentState[1]
            for node in expanded:
                if (node[0] not in explored):
                    queue.push((node[0], list(pathTillCurrent + [node[1]])))


    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    priorityQueue = util.PriorityQueue()
    directionStack = util.Stack()
    startState = problem.getStartState();

    explored = set();
    augmentedStartState = (startState,[])
    priorityQueue.update(augmentedStartState,0);
    costFromStartNode ={}
    costFromStartNode[augmentedStartState[0]] =0;


    while (priorityQueue.isEmpty() == False):
        currentState = priorityQueue.pop();
        if (problem.isGoalState(currentState[0])):
            return currentState[1]
        else:
            expanded = problem.getSuccessors(currentState[0]);
            explored.add(currentState[0]);
            pathTillCurrent = currentState[1]
            for node in expanded:
                if (node[0] not in explored ):
                    if(node[0] in costFromStartNode):
                        currentCost = costFromStartNode[currentState[0]] + node[2];
                        previousCost = costFromStartNode[node[0]];
                        if(currentCost < previousCost):
                            costFromStartNode[node[0]] = currentCost
                            priorityQueue.update((node[0],list(pathTillCurrent + [node[1]])), costFromStartNode[node[0]])
                    else:
                        costFromStartNode[node[0]] = costFromStartNode[currentState[0]] + node[2]
                        priorityQueue.update((node[0],list(pathTillCurrent + [node[1]])), costFromStartNode[node[0]])



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
    priorityQueue = util.PriorityQueue()
    directionStack = util.Stack()
    startState = problem.getStartState();

    explored = set();
    augmentedStartState = (startState, 'START', 0)
    priorityQueue.update(augmentedStartState, augmentedStartState[2]);
    costFromStartNode ={}
    Directiondict = {}
    costFromStartNode[augmentedStartState[0]] =0

    while (priorityQueue.isEmpty() == False):
        currentState = priorityQueue.pop();
        if (problem.isGoalState(currentState[0])):
            directions = util.Stack();
            directions.push(currentState[1])
            current = currentState
            while (current != augmentedStartState):
                directions.push(Directiondict[current][1]);
                current = Directiondict[current];
            directions.list.reverse()
            print(' '.join(directions.list[1:]));
            return (directions.list[1:])
        else:
            expanded = problem.getSuccessors(currentState[0]);
            explored.add(currentState[0]);
            for node in expanded:
                if (node[0] not in explored):
                    if (node[0] in costFromStartNode):
                        currentCost = costFromStartNode[currentState[0]] + node[2];
                        previousCost = costFromStartNode[node[0]];
                        if (currentCost < previousCost):
                            costFromStartNode[node[0]] = currentCost
                            priorityQueue.update(node, costFromStartNode[node[0]] + heuristic(node[0],problem))
                            Directiondict[node] = currentState
                    else:
                        costFromStartNode[node[0]] = costFromStartNode[currentState[0]] + node[2]
                        priorityQueue.update(node, costFromStartNode[node[0]] + heuristic(node[0],problem))
                        Directiondict[node] = currentState

    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
