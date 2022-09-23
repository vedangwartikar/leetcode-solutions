class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        combinations = []
        
        def backtrack(i, curr_str):
            if len(curr_str) == len(digits):
                combinations.append(curr_str)
                return
            for char in digits_map[digits[i]]:
                backtrack(i + 1, curr_str + char)
        
        if digits:
            backtrack(0, "")
        
        return combinations
                