class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        def firstRow(s: string) -> bool:
            s = s.lower()
            row1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}

            for i in s:
                if i not in row1: 
                    return False
            
            return True

        def secondRow(s: string) -> bool:
            s = s.lower()
            row2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
            for i in s:
                if i not in row2:
                    return False
            
            return True

        def thirdRow(s: string) -> bool:
            s = s.lower()
            row3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
            for i in s:
                if i not in row3:
                    return False
            
            return True

        arr = []

        for i in words:
            if firstRow(i):
                arr.append(i)
            elif secondRow(i):
                arr.append(i)
            elif thirdRow(i):
                arr.append(i)

        return arr


    
    