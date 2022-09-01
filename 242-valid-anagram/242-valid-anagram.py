class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Create an array of size 26. For all elements in s, increment the letter index (ord) by 1 and for all elements in t, decrement the letter index by 1. At the end traverse the letter array and return False if any element is not equal to 0. Else, return True
        
        letter_array = [0]*26
        for each_letter in s:
            letter_array[ord(each_letter) - ord('a')] += 1
        for each_letter in t:
            letter_array[ord(each_letter) - ord('a')] -= 1
        for i in letter_array:
            if i != 0:
                return False
        return True
        
        # Count approach - Working
        
        # if len(s) != len(t):    return False
        # s_dict, t_dict = {}, {}
        # for i in range(len(s)):
        #     if s[i] not in s_dict:
        #         s_dict[s[i]] = 1
        #     else:
        #         s_dict[s[i]] += 1
        #     if t[i] not in t_dict:
        #         t_dict[t[i]] = 1
        #     else:
        #         t_dict[t[i]] += 1
        # for each_letter in s_dict:
        #     if each_letter not in t_dict or s_dict[each_letter] != t_dict[each_letter]:
        #         return False
        # return True
                
                