// https://leetcode.com/problems/contains-duplicate-ii/
// https://leetcode.com/submissions/detail/280087425/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    if(nums.length <= k){
        let mySet = new Set(nums);
        return mySet.size != nums.length;
    }

    let object = {};

    for(let i  = 0; i < nums.length; i++){
        if(object[nums[i]] == undefined) {
            object[nums[i]] = [i];
        }else{

            for(let j = 0; j < object[nums[i]].length; j++){
                if(Math.abs(object[nums[i]][j] - i) <= k){
                    return true;
                }
            }

            object[nums[i]].push(i);
        }
    }

    return false;
};
