class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list(pattern)
        s = s.split(' ')
        if len(pattern) != len(s): return False
        follow = {}
        for a, b in zip(pattern, s):
            if a not in follow:
                for x in follow:
                    if follow[x] == b:
                        return False
                follow[a] = b
            else:
                if follow[a] != b:
                    return False
        return True