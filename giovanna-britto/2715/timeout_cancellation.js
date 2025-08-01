/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    const cancelaFuncao = function (){
        clearTimeout(timer);
    };

    const timer = setTimeout(()=>{
        fn(...args)
    }, t);

    return cancelaFuncao;
};

