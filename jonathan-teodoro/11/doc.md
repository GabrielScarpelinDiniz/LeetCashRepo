class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            h = min(height[l], height[r])
            w = r - l
            area = h * w
            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area

essa foi mais treta. usei two pointer, mas como?
dois ponteiros um no inicio e um no final. faco o calculo da area com eles e comparo com a maior area que temos até agora. Apos isso, eu pego a menor coluna e and com ela, se for a l ára a direita e se for a r pra esquerda.