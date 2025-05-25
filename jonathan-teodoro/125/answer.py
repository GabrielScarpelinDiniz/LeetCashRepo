class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphabet = "abcdefghijklmnopqrstuvwxyz1234567890"
        teste = ""
        for i in s:
            if i in alphabet:
                teste += i
        print(teste)
        l = 0
        r = len(teste)-1

        while l<=r:
            print(teste[l], teste[r])
            if teste[l] == teste[r]:
                l +=1
                r -= 1
                continue
            else:
                return False
            l +=1
            r -= 1
        
        return True