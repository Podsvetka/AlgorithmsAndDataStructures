from algorithms.SecondPractice.practice import Flamingo


class Node:

    def __init__(self, data: Flamingo):
        self.data = data    #type: Flamingo
        self.next = None    #type: [Node, None]

    def has_value(self, value: Flamingo):
        """method to compare the value with the node data"""
        if self.data is value:
            return True
        else:
            return False

    def __repr__(self):
        return self.data