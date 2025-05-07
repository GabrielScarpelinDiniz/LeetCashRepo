class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        print(words)

        l = 0
        r = len(words)-1


        while l<=r:
            words[l],words[r] = words[r],words[l]
            l +=1
            r-=1
        
        string = ''
        for i in range(len(words)):
            if words[i] == '':
                continue
            string += words[i]
            string += ' '
        
        return string[:-1]
            
