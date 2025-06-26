class Solution:
    def minOperations(self, boxes):
        n = len(boxes)
        answer = [0] * n

        count = 0  
        ops = 0    
        for i in range(n):
            answer[i] += ops
            if boxes[i] == '1':
                count += 1
            ops += count

        count = 0
        ops = 0
        for i in range(n - 1, -1, -1):
            answer[i] += ops
            if boxes[i] == '1':
                count += 1
            ops += count

        return answer
