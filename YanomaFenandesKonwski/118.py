class Solution(object):
    def generate(self, numRows):
        lista = []
        i=0
        j=0
        for i in range(numRows):
            if i==0:
                lista.append([1])
            else:
                listadentro = []
                for j in range(i+1):
                    if j==0:
                        listadentro.append(1)
                    elif j==i:
                        listadentro.append(1)
                    else:
                        listadentro.append(lista[i-1][j]+lista[i-1][j-1])
                lista.append(listadentro)
        return lista

        