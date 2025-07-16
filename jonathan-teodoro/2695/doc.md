

/**
 * @param {number[]} nums
 * @return {void}
 */
var ArrayWrapper = function(nums) {
    this.nums = nums;
};

/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function() {
    return this.nums.reduce((sum, num) => sum + num, 0);
}

/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function() {
    return `[${this.nums.join(",")}]`;
}
O código define uma classe que permite somar dois objetos ArrayWrapper (isso é feito implementando o método valueOf, que retorna a soma dos elementos do array). Ao usar o operador +, o JavaScript chama automaticamente esse método para obter um valor numérico.
Ele também permite exibi-los como uma string no formato [1,2,3], graças à implementação do método toString, que transforma o array em uma string com colchetes e vírgulas.
Ao sobrescrever valueOf e toString, o objeto se comporta de forma personalizada ao ser somado ou convertido para string.