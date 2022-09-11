class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = {}
        result = 0
        for i in words:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        for j in count.copy():
            if count[j] > 0:
                if j[::-1] in count and j[0] != j[1]:
                    counterparts = min(count[j], count[j[::-1]])
                    result += 4*counterparts
                    count[j] -= counterparts
                    count[j[::-1]] -= counterparts
                if j[0] == j[1]:
                    if count[j] > 1 and count[j] % 2:
                        result += (count[j] - 1)*2
                        count[j] -= 1
                    elif count[j] > 1 and not count[j] % 2:
                        result += count[j]*2
                        count[j] = 0
        for k in count:
            if k[0] == k[1] and count[k] > 0:
                result += 2
                break
        return result