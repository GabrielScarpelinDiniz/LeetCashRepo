class Solution(object):
    def flipAndInvertImage(self, image):
        for row in image:
            esquerda, direita = 0, len(row) - 1
            while esquerda <= direita:
                if esquerda == direita:
                    row[esquerda] = 1 - row[esquerda]
                else:
                    row[esquerda], row[direita] = 1 - row[direita], 1 - row[esquerda]
                esquerda += 1
                direita -= 1
        return image