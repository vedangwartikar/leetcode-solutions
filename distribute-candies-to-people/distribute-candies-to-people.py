class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        idx = 0
        val = 1
        arr = [0]*num_people
        while candies > 0:
            arr[idx] += val
            idx += 1
            candies -= val
            val += 1
            if idx == num_people:
                idx = 0
            if val > candies:
                val = candies
        return arr