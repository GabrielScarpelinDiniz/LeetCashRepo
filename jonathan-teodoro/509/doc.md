func fib(n int) int {
    if n < 2 {
        return n
    }
    prev, cur := 0, 1
    for i := 2; i <= n; i++ {
        prev, cur = cur, prev+cur
    }
    return cur
}

sei uma abordagem iterativa pro Fibonacci por ser mais eficiente que a recursiva em termos de espaço e tempo. Começo tratando os casos base, quando n < 2. Depois uso duas variáveis, prev e cur, pra armazenar os dois últimos valores da sequência e vou atualizando com um for simples. No final, cur tem o resultado. Essa abordagem evita stack overflow e roda em tempo linear com espaço constante