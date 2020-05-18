// https://leetcode.com/problems/string-to-integer-atoi/
// https://leetcode.com/submissions/detail/270932187/

/**
 * @param {string} str
 * @return {number}
 */
var myAtoi = function(str) {
    if(str === undefined || typeof str != "string") throw new Error("Invalid input");

    if(/[^\s]/g.test(str) === false || str === "-" || str === "+") return 0;

    let first_char = str.match(/[^\s]/)[0];

    if(/[\-\+0-9]/.test(first_char) == false){
        return 0;
    }

    let number = parseInt(str);

    if(isNaN(number)){
        return 0;
    }

    if(number === ToInt32(number)){
       return number;
    } else {
         if(number < 0) {
             return Math.pow(-2, 31);
         } else {
             return Math.pow(2, 31)-1;
         }
    }

};

function ToInt32(x) {
    return x | 0;
}
