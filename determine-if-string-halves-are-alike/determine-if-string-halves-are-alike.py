class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return len(list(filter(lambda x: x in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'],s[:int(len(s)/2)]))) == len(list(filter(lambda x: x in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'],s[int(len(s)/2):])))