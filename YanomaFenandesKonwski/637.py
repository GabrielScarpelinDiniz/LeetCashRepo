class Solution(object):
    def averageOfLevels(self, root):
        if not root:
            return []

        fila = [root]
        resultado = []

        while fila:
            total = 0
            tamanho = len(fila)
            
            for _ in range(tamanho):
                no = fila.pop(0)  
                total += no.val
                
                if no.left:
                    fila.append(no.left)
                if no.right:
                    fila.append(no.right)
            
            resultado.append(total / float(tamanho))

        return resultado