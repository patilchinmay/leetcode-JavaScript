// https://leetcode.com/problems/remove-element/
// https://leetcode.com/submissions/detail/273098867/

/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {

    for(let i = nums.length-1;  i >= 0; i--){

        if(val == nums[i] ){
            nums.splice(i, 1);
        }
    }

    return nums.length;
};
