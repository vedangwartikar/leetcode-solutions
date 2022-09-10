class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Filter out the non-alphanumeric characters (use filter()) and make all characters lowercase
        Use 2 pointer approach - traverse from left and right and return False if the characters don't match
        """
        alnum_string = ''.join(filter(str.isalnum, s)).lower()
        left, right = 0, len(alnum_string) - 1
        if len(alnum_string) <= 1: return True
        while left <= right:
            if alnum_string[left] != alnum_string[right]:
                return False
            left += 1
            right -= 1
        return True