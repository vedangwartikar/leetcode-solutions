class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Create a count (a at 0, b at 25,... z at 25) for each string and map the counted array to each string
        Match the counter array and store the anagram strings with the same key as counter
        Counter stores key tuple([0,1,1,1,0,...]) with values ["bcd", "cdb", "dcb"]
        Return the value of resultant list (without the count)
        """
        result = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            result[tuple(count)].append(string)
        return result.values()
            