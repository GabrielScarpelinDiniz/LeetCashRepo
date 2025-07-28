A ideia aqui é compor funções, ou seja, fazer com que o resultado de uma função seja passado como entrada para a próxima, da direita para a esquerda. Se temos [f1, f2, f3], queremos que o valor entre em f3, o resultado vá para f2, e o resultado final vá para f1.

Para isso, usamos reduceRight, que é como o reduce normal, mas começa do fim do array. O valor inicial é o x passado, e cada função é aplicada em cima do acumulador. Assim conseguimos simular f1(f2(f3(x))).

Se o array estiver vazio, o reduceRight apenas retorna x, que é o comportamento esperado (identidade).

É uma forma elegante e funcional de compor lógica de forma encadeada.

/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return function(x) {
        return functions.reduceRight((acc, fn) => fn(acc), x);
    };
};

/**
 * Exemplo de uso:
 * const fn = compose([x => x + 1, x => x * x, x => 2 * x]);
 * console.log(fn(4)); // 65
 */
