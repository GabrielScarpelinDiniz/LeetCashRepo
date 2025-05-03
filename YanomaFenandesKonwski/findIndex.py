strings = "butsad"
encontrar = "sad"

def strStr(strings, encontrar):
    i=0
    encontrando =""
    while len(strings) - len(encontrar)>=i:
        j=0
        while j<len(encontrar) and strings[i+j]==encontrar[j]:
            j+=1
            if j == len(encontrar):
                return i
        i+=1
    return -1
print(strStr(strings, encontrar))
                


