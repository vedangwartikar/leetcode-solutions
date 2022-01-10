class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        arr, hashmap, ans = [], {}, []
        self.recursive_permute(nums, arr, hashmap, ans)
        return ans
        
    def recursive_permute(self, nums, arr, hashmap, ans):
        if len(arr) == len(nums):
            ans.append(arr[:])
            return
        for i in nums:
            if i not in hashmap or not hashmap[i]:
                hashmap[i] = True
                arr.append(i)
                self.recursive_permute(nums, arr, hashmap, ans)
                arr.pop(-1)
                hashmap[i] = False