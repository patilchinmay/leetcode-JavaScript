// https://leetcode.com/problems/contains-duplicate/
// https://leetcode.com/submissions/detail/280079537/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let mySet = new Set(nums);
    return mySet.size != nums.length;
};
