/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    dicS = {}
    arrS = []

    for(let i = 0; i < s.length; i++){
        if(s[i] in dicS){
            arrS.push(dicS[s[i]])
        }else{
            dicS[s[i]] = i
            arrS.push(i)
        }
    }

    console.log(dicS)
    console.log(arrS)

    dicT = {}
    arrT = []

    for(let i = 0; i < t.length; i++){
        if(t[i] in dicT){
            arrT.push(dicT[t[i]])
        }else{
            dicT[t[i]] = i
            arrT.push(i)
        }
    }

    return JSON.stringify(arrT) == JSON.stringify(arrS)
};