class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return dict(sorted(dict(map(lambda key, value : (key, value) , heights, names)).items(), reverse=True)).values()