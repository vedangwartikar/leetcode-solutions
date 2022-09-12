class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string not in hashmap:
                hashmap[sorted_string] = [string]
            else:
                hashmap[sorted_string].append(string)
        result = []
        for i in hashmap:
            result.append(hashmap[i])
        return result