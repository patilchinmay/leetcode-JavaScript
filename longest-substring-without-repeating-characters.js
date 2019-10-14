// https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
// https://leetcode.com/submissions/detail/269809054/

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    if(s == undefined || typeof s != "string") throw new Error("Invalid Input");

    let lengthOfString = s.length;

    let longestSubstringLength = 0;

    outer:
        for(let i = 0 ; i < lengthOfString; i++){
    inner:
            for(let j = i+1; j <= lengthOfString; j++){

                if(j-i > longestSubstringLength){
                    let subString = s.substring(i,j);
                    if(subString.length > longestSubstringLength){
                        // new Set(subString.split('')).size == subString.length
                        if(!/(.).*\1/.test(subString)){
                            console.log(subString);
                            if(subString.length > longestSubstringLength){
                                longestSubstringLength = subString.length;
                            }
                        }else{
                            break inner;
                        }
                    }
                }
            }
        }

    return longestSubstringLength;
};
