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
        util.raiseNotDefined() ## TODO

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined() ## TODO

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined() ## TODO

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined() ## TODO


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
    """Cost of each weight is assumed to be 0 so the first solution is chosen"""

    "*** YOUR CODE HERE ***"

    visited = set()
    stack = [ ]
    stack.append( (problem.getStartState(), [ ]) )
    while len(stack) != 0:
        current_state, current_path = stack.pop()
        if problem.isGoalState( current_state ):
            return current_path
        elif current_state in visited:
            continue
        else:
            visited.add(current_state)
            for next_state, next_transition, next_weight in problem.getSuccessors(current_state):
                stack.append((next_state, current_path + [next_transition]))
                return None

    util.raiseNotDefined() ## TODO

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    """Cost of each weight is assumed to be 0 so the first solution is chosen"""
    "*** YOUR CODE HERE ***"

    visited = set()
    queue = [ ]
    queue.append( (problem.getStartState(), [ ]) )
    while len(queue) != 0:
        current_state, current_path = queue.pop( 0 )
        if problem.isGoalState( current_state ):
            return current_path
        elif current_state in visited:
            continue
        else:
            visited.add(current_state)
            for next_state, next_transition, next_weight in problem.getSuccessors(current_state):
                queue.append((next_state, current_path + [next_transition]))
                return None

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    """Each weight between nodes has the same weight and is therefore uniform"""
    "*** YOUR CODE HERE ***"

    visited = set()
    priority_queue = util.PriorityQueue()
    priority_queue.push((problem.getStartState(), [ ], 0), 0)
    while not priority_queue.isEmpty():
        current_state, current_path, current_weight = priority_queue.pop()
        if problem.isGoalState( current_state ):
            return current_path
        elif current_state in visited:
            continue
        else:
            visited.add(current_state)
            for next_state, next_transition, next_weight in problem.getSuccessors(current_state):
                priority_queue.push((next_state, current_path + [next_transition], current_weight + next_weight), current_weight + next_weight)
                return None

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined() ## TODO


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
