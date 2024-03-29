class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2:  # odd number of brackets
            return False

        closed = {'(': ')', '{': '}', '[': ']'}
        stack = ['']  # adding one element so that stack is empty error don't occur

        for bracket in s:

            if bracket in closed.keys():  # closed.keys() -> opened
                stack.append(closed[bracket])

            elif bracket != stack.pop():
                return False

        return stack == ['']
