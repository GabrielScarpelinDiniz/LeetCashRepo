/**
 * @param {Function} fn
 * @param {number} t milliseconds
 * @return {Function}
 */
var debounce = function(fn, t) {
    let timeoutId;

    return function(...args) {
        if (timeoutId) clearTimeout(timeoutId);

        timeoutId = setTimeout(() => {
            fn(...args);
        }, t);
    };
};

mplementei uma função debounce que retorna uma nova função e adia a execução da original (fn) até que um tempo t passe sem novas chamadas. Uso um setTimeout e cancelo o anterior com clearTimeout sempre que a função é chamada novamente. Isso garante que fn só execute após a última chamada, útil para evitar execuções repetidas, como em eventos de digitação.