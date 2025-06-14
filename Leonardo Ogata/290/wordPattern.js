/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
    let dicPattern = {}
    let arrPattern = []

    for(let i = 0; i < pattern.length; i++){
        if (pattern[i] in dicPattern){
            arrPattern.push(dicPattern[pattern[i]]);
        }else{
            dicPattern[pattern[i]] = i;
            arrPattern.push(i);
        }
    }

    wordsArray = s.split(" ")


    let dicS = Object.create(null);
    let arrS = []

    for(let i = 0; i < wordsArray.length; i++){
        if (wordsArray[i] in dicS){
            arrS.push(dicS[wordsArray[i]]);
        }else{
            dicS[wordsArray[i]] = i;
            arrS.push(i);
        }
    }

    console.log(arrS)
    console.log(arrPattern)

    return JSON.stringify(arrS) == JSON.stringify(arrPattern)
};