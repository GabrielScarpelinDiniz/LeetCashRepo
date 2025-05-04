class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(' ')
        answer = []
        for i in range(len(arr)):
            if len(arr[i]) >= 1:
                answer.append(arr[i])
        print(answer)
        return len(answer[-1])

