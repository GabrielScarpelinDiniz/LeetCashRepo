s = "anagram"
t = "nagaram"

def isAnagram(s: str, t: str):
    def contar_letras(palavra):
        dicionario = {}
        for letra in palavra:
            if letra in dicionario:
                dicionario[letra] += 1
            else:
                dicionario[letra] = 1
        return dicionario

    dicionario_s = contar_letras(s)
    dicionario_t = contar_letras(t)

    return dicionario_s == dicionario_t
    
print(isAnagram(s,t))