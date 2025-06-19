class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        diferenca = 0

        for i in range(1, len(points)):
            diferenca = max(diferenca, points[i][0] - points[i-1][0])
        
        return diferenca