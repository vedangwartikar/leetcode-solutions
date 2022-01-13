class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
        
        heap = []
        for word in d:
            heapq.heappush(heap, (-d[word], word))
        print(heap)
        
        answer = []
        for _ in range(k):
            freq, word = heapq.heappop(heap)
            answer.append(word)
        
        return answer