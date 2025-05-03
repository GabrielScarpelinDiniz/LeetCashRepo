strs = ["flower", "flow", "flight"]


def transformString(lista):
    prefixo = {}
    prefixo = strs[0]
    for s in strs[1:]:
        i = 0

        while len(prefixo)>i and i<len(s) and prefixo[i] == s[i]:
            i+=1
        prefixo = prefixo[:i] 

        if not prefixo:
            break
    return prefixo

print(transformString(strs))

# código feito para testes localmente, aí no exercício só usei o nome da função original do leetcode e deixei sem o print