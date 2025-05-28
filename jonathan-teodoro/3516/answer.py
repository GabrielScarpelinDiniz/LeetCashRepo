class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        distancia_x = x - z
        distancia_y = y - z
        if abs(distancia_x) < abs(distancia_y):
            return 1
        elif abs(distancia_y) < abs(distancia_x):
            return 2
        else:
            return 0