class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        selecionadas = set(allowed)
        cont = 0

        for palavra in words:
            for letras in palavra:
                if letras not in selecionadas:
                    cont += 1
                    break

        return len(words) - cont