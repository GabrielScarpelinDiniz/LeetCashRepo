class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        tempo_total = 0
        for i in range(1, len(points)):
            x_anterior, y_anterior = points[i - 1]
            x_atual, y_atual = points[i]
            diferenca_x = abs(x_atual - x_anterior)
            diferenca_y = abs(y_atual - y_anterior)
            tempo_total += max(diferenca_x, diferenca_y)
        return tempo_total
        