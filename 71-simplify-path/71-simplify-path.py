class Solution:
    def simplifyPath(self, path):
        stack = []
        for i in path.split("/"):
            if stack and i == "..":
                stack.pop()
            if i not in ['', '.', '..']:
                stack.append(i)
        return '/{}'.format('/'.join(stack))