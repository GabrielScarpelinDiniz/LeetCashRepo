def permute(nums):
    resultado = []

    def combinatoria(caminho, restantes):
        if not restantes:
            resultado.append(caminho)
            return
        for i in range(len(restantes)):
            novo_caminho = caminho + [restantes[i]]
            novos_restantes = restantes[:i] + restantes[i+1:]
            combinatoria(novo_caminho, novos_restantes)
    combinatoria([], nums)
    return resultado

print(permute([1, 2, 3]))