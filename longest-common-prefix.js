// https://leetcode.com/problems/longest-common-prefix/
// https://leetcode.com/submissions/detail/271038913/

/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if(strs == undefined || strs.length == 0) return "";

    let smallestIndex = 0;
    let smallest = strs[0];

    strs.map((value, index)=>{
        if(value.length < smallest.length){
            smallestIndex = index;
            smallest = value;
        }
    });

    strs.splice(smallestIndex, 1);

    let longestMatch = "";

    for(let i = smallest.length; i >= 0; i--){
        let subString = smallest.substring(0, i);
        // console.log(`${subString}`);

        if(matchAcrossArray(strs, subString)){
            // console.log(`Lonegest Prefix Match : ${subString}`);
            longestMatch = subString;
            break;
        }
    }

    return longestMatch;
};

function matchAcrossArray(arr, pattern){
    let matchesAll = true;

    for(let i = 0; i < arr.length; i++) {
        if(arr[i].startsWith(pattern) == false){
            matchesAll = false;
            break;
        }
    }

    return matchesAll;
}
