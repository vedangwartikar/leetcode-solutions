class Solution:
    def isValid(self, s: str) -> bool:
        """
        Create an array and a dictionary to maintain paranthesis
        If the counterpart of the current paranthesis is not available in the stack append to the stack
        Else check if the counterpart i available - then pop the counterpart from the stack
        Return True is the stack is empty at the end, else False
        * Return False directly if a closing bracket is found
        """
        if len(s) < 2: return False
        stack = []
        dict = {'}': '{', ']': '[', ')': '('}
        for i in s:
            if i not in dict:
                stack.append(i)
            elif len(stack) and dict[i] == stack[-1]:
                    stack.pop(-1)
            else:
                return False
        return stack == []