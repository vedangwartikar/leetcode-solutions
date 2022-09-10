class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        create 2 pointers - small and large
        loop till the addition of small and large array elements equals the target value
        if the total of small and large array elements is greater than the target, decrease the large pointer
        else if the total of small and large array elements is smaller than the target, increase the small pointer
        O(n) with O(1) extra space
        """
        smaller, larger = 0, len(numbers) - 1
        while numbers[smaller] + numbers[larger] != target:
            if numbers[smaller] + numbers[larger] > target:
                larger -= 1
            elif numbers[smaller] + numbers[larger] < target:
                smaller += 1
        return [smaller + 1, larger + 1]