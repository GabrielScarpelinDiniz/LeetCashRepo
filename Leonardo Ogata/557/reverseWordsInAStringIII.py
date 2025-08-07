class Solution:
    def reverseWords(self, s: str) -> str:
        right = 0
        ans = ""
        temp = ""


        while right < len(s):
            if s[right] == " ":
                temp = temp[::-1]
                temp += s[right]
                ans += temp
                temp = ""
            else:
                temp += s[right]
            
            right += 1

        if temp:
            ans += temp[::-1]

        return ans