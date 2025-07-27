Exercicio muito facil, so preciso adicionar uma promisse passando um setTimeout do tempo em millis passado na questão. Exercicio iditoa só para ser entregue. Uma linha de codigo.
/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    return new Promise(resolve => setTimeout(resolve, millis));
}

/** 
 * let t = Date.now();
 * sleep(100).then(() => console.log(Date.now() - t)); // ~100
 */
