class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        montanha = []
        for i in range(1, len(height)):
            if (height[i-1] > threshold):
                montanha.append(i)

        return montanha