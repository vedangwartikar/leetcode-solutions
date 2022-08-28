class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        point_dict = {}
        for each_point in range(len(points)):
            point_dict[each_point] = points[each_point][0]**2 + points[each_point][1]**2
        sorted_point_dict = dict(sorted(point_dict.items(), key = lambda coordinate: coordinate[1]))
        answer, count = [], 0
        for each in sorted_point_dict:
            if count < k:
                answer.append(points[each])
            count += 1
        return answer