class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        neWord = []
        i,j = 0,0

        while (i < len(word1) or j < len(word2)):
            if (i< len(word1)):
                neWord.append(word1[i])
                i += 1
            if (j < len(word2)):
                neWord.append(word2[j])
                j += 1

        return ''.join(neWord)