class Solution:
    def reorganizeString(self, s: str) -> str:
        #create a hashmap to store counts of letters
        hashmap = {}
        for letter in s:
            if letter not in hashmap:
                hashmap[letter] = 1
            else:
                hashmap[letter] += 1
        
        # max-heapify the hashmap
        from heapq import heappush, heappop
        h = []
        for letter in hashmap:
            heappush(h, (-hashmap[letter], letter))
        
        # append the most frequent current and next letter to ensure that current letter is not repeated
        res = ""
        while len(h) > 1:
            current_count, current = heappop(h)
            next_count, next = heappop(h)
            
            res += current
            res += next
            
            if abs(current_count) > 1:
                heappush(h, (current_count + 1, current))
            if abs(next_count) > 1:
                heappush(h, (next_count + 1, next))
        # check for last letter, if there are mre than 2 same letters then reorganizing is not possible.. else append to the res
        if h:
            last_count, last = h[0]
            if abs(last_count) > 1:
                return ""
            else:
                res += last
        return res
        return ""