/**
 * @param {Function} fn 
 * @param {Array} args 
 * @param {number} t 
 * @return {Function} 
 */
function cancellable(fn, args, t) {
    const timeoutId = setTimeout(() => {
        fn(...args);
    }, t);

    const cancelFn = () => {
        clearTimeout(timeoutId);
    };

    return cancelFn;
}
Essa função retorna um cancelFn que pode cancelar a execução atrasada da função fn. Ao chamarmos cancellable(fn, args, t), agendamos a execução de fn(...args) para ocorrer após t milissegundos. No entanto, se cancelFn for chamado antes desse tempo, a execução é cancelada com clearTimeout, impedindo que fn rode.