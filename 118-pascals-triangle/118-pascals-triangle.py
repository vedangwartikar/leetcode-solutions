class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1],[1,1]]
        if numRows == 1:
            return [pascal[0]]
        if numRows == 2:
            return pascal
        for i in range(numRows-2):
            arr = []
            add = 0
            for j in range(len(pascal[-1])-1):
                print(pascal[-1])
                add = pascal[-1][j] + pascal[-1][j+1]
                arr.append(add)
            arr = [1] + arr + [1]
            pascal.append(arr)
        return pascal
