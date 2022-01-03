class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        hashmap = {'(': ')', '[': ']', '{': '}'}
        for i in range(len(s)):
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
            else:
                if len(stack) and s[i] == hashmap[stack[-1]]:
                    stack.pop(-1)
                else:
                    return False
        return stack == []