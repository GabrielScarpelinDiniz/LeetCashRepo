class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = 0
        for num_of_candies in candies:
            if num_of_candies > max_candies:
                max_candies = num_of_candies
        
        print(max_candies)
        answer = []
        for i in candies:

            if i+extraCandies>=max_candies:
                answer.append(True)
            else:
                answer.append(False)

        print(answer)
        return answer
        

                    