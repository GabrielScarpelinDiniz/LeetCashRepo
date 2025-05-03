class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        for i in range(len(flowerbed)):
            if i == 0:
                if (len(flowerbed) == 1 or flowerbed[i + 1] == 0) and flowerbed[i] == 0:
                    print('entrou 1')
                    n -= 1
                    flowerbed[i] = 1

            elif i == len(flowerbed) - 1:
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                    print('entrou 2')
                    n -= 1
                    flowerbed[i] = 1

            elif flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                print('entrou 3')
                n -= 1
                flowerbed[i] = 1

        print(flowerbed)
        return n <= 0
