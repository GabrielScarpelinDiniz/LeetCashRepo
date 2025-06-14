class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1Conc = ''.join(word1)
        word2Conc = ''.join(word2)

        if (word1Conc == word2Conc):
            return True
        else:
            return False
        