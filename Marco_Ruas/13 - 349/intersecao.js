/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    let intersecao = []
    let existe = {}

    for(let i = 0; i < nums1.length; i++){
        for(let j = 0; j < nums2.length; j++){
            if(nums1[i] === nums2[j] && existe[nums1[i]] !== true){
                intersecao.push(nums1[i]);
                existe[nums1[i]] = true;
                break;
            }
        }
    }
};