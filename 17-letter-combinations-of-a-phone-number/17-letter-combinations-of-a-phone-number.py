"""
Create a hashmap of digits and their strings
Create a backtracking function that appends generated_str to resultant array if the len(generated_str) is same as len(digits) and then returns back
Else, for each character in the digit string call the backtracking with the next digit's index (index + 1) and updated string (curr_str + char of new string)
Call backtrack with index 0 and an empty string if digits string exists
In the end return combinations array
O(4^n)
"""
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
                print(i + 1, curr_str + char)
                backtrack(i + 1, curr_str + char)
        
        if digits:
            backtrack(0, "")
        
        return combinations
                