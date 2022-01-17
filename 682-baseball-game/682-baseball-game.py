class Solution:
    def calPoints(self, ops: List[str]) -> int:
        arr = []
        for i in ops:
            try:
                arr.append(int(i))
            except:
                if i == 'C':
                    arr.pop(-1)
                elif i == 'D':
                    arr.append(int(arr[-1]*2))
                else:
                    arr.append(int(arr[-1]) + int(arr[-2]))
        return sum(arr)