# Two sum

Já que mandaram eu fazer, tamo fazendo tamo fazendo.

Encontra dois números em um array que somam um valor alvo específico.
Este método diz que cada entrada terá exatamente uma solução, e o mesmo elemento não pode ser usado duas vezes.

Usando uma tabela hash de apoio, eu não preciso percorrer duas vezes o array, já que eu salvei os valores que eu já passei e só verifico se o número faltante para o target está no dicionário.

**Complexidade de Tempo:** O(n), onde n é o número de elementos em `nums`.
Isso ocorre porque o algoritmo faz uma única passagem pelo array, e as operações no dicionário (`Add`, `ContainsKey`) têm um custo médio de O(1).

**Complexidade de Espaço:** O(n) no pior caso. O dicionário pode armazenar até n-1 elementos se o par da solução for encontrado no final do array.
