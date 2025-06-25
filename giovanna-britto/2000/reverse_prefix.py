class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if (ch in word):
            sel = list(word[:word.index(ch)+1])
            letras = list(word[word.index(ch)+1:])
            sel.reverse()
            return ''.join(sel+letras)
        else:
            return word
        
        