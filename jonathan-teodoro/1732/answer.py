class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        answer = [0]

        sum = 0
        for i in gain:
            sum += i
            answer.append(sum)
        print(answer)

        max = float('-inf') 
        for i in answer:
            if i > max:
                max = i
        return max