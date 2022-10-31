class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1: return 1
        i = 0
        n = len(s)
        visited = set()
        length = 0
        max_length = 0
        while i < n:
            if not visited:
                visited.add(s[i])
                length = 1
                i += 1
            else:
                if s[i] in visited:
                    j = i - 1
                    while j >= 1:
                        if s[j] == s[i]:
                            break
                        j -= 1
                    i = j + 1
                    visited.clear()
                    length = 0
                else:
                    visited.add(s[i])
                    length += 1
                    i += 1
            max_length = max(max_length, length)
        return max_length