class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = "aeiou"
        count_vowels = [0] * 26
        count_consonants = [0] * 26

        for ch in s:
            idx = ord(ch) - ord('a')
            if ch in vowels:
                count_vowels[idx] += 1
            else:
                count_consonants[idx] += 1

        max_vowel = max(count_vowels) if sum(count_vowels) > 0 else 0
        max_consonant = max(count_consonants) if sum(count_consonants) > 0 else 0

        return max_vowel + max_consonant

        Aqui a gente tem duas listas de tamanho 26, uma pra contar cada letra que for vogal e outra pras consoantes. A gente pega o código ASCII da letra pra saber o índice na lista e soma um na posição correta. Depois, só acha o maior número de cada lista — o que representa a letra que mais apareceu. Soma esses dois e retorna o resultado.