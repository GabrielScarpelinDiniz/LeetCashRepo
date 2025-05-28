
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxWord = 0
        
        for i in sentences:
            word = len(i.split())
            if(word >= maxWord):
                maxWord = word

        return maxWord
