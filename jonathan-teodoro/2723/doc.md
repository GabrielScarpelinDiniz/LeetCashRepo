/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    return Promise.all([promise1, promise2])
        .then(([val1, val2]) => val1 + val2);
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */

 Promise.all([promise1, promise2]) retorna uma nova promise que resolve quando ambas as promessas foram resolvidas. O .then(([val1, val2]) => val1 + val2) soma os dois valores resolvidos. O retorno é uma promise que resolve com essa soma.