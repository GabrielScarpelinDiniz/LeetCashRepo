func pivotIndex(nums []int) int {
    totalSum := 0
    leftSum := 0

    for _, num := range nums {
        totalSum += num
    }

    for i, num := range nums {
        totalSum -= num

        if leftSum == totalSum {
            return i
        }

        leftSum += num
    }

    return -1
}


O código primeiro calcula a soma total do array para saber o valor da “direita” inicial. Depois, ele itera pelos elementos, atualizando a soma da esquerda e subtraindo o elemento atual da soma total para representar a soma da direita. A cada passo, verifica se as duas somas são iguais — se forem, esse índice é o pivô e é retornado. Se não encontrar nenhum, retorna -1. A solução é eficiente porque faz só uma passada no array, usando espaço constante.