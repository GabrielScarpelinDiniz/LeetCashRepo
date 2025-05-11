class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        vowels_arr = []
        for i in s:
            if i in vowels:
                vowels_arr.append(i)

        reverse = vowels_arr[::-1]
        index = 0
        answer = ''
        for i in s:
            if i in vowels:
                answer += reverse[index]
                index += 1
            else: 
                answer += i

                
        return answer