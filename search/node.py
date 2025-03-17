


class Node:

    def __init__(self, parent, action, depth, cost, state):
        self.parent = parent
        self.action = action
        self.depth = depth
        self.cost = cost
        self.state = state

    def __repr__(self):
        return str(self.state)

    def expand(self, problem):
        successors = []
        for new_state, action in problem.successors(self.state):
            # self it means i will be always the parent of the new states that i will create by expanding, and I was choosen in the fringe by a well-done strategy
            successors += [Node(self, action, self.depth+1, self.cost+problem.cost(self.state, action), new_state)]
            #successors.append(Node(self, action, self.depth+1, self.cost+problem.cost(self.state, action), state))
        return successors

    def solution(self):
        path = []
        node = self

        while node.parent is not None:
            path.append(node.action)
            node = node.parent

        return path[::-1]

