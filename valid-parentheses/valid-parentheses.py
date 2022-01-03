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
                try:
                    if s[i] == hashmap[stack[-1]]:
                        stack.pop(-1)
                    else:
                        return False
                except:
                    return False
        if len(stack):
            return False
        return True