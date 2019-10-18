// https://leetcode.com/problems/reverse-integer
// https://leetcode.com/submissions/detail/270898996/

/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    if(x === undefined || typeof x != "number") throw new Error("Invalid Input");

    if(x%10 == 0) x = x/10;

    let isNegative = false;

    if(x<0) {
        isNegative = true;
        x = x * -1;
    }

    x = Number(`${x}`.split('').reverse().join(''));

    if(isNegative){
         x = x * -1;
    }

    if(x == ToInt32(x)){
        return x;
    } else {
        return 0;
    }

};

function ToInt32(x) {
    return x | 0;
}
