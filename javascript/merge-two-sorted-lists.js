// https://leetcode.com/problems/merge-two-sorted-lists/
// https://leetcode.com/submissions/detail/271900267/

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {

    let ans = [];

    while(l1 != null){
        ans.push(l1.val);
        l1 = l1.next;
    }

    while(l2 != null){
        ans.push(l2.val);
        l2 = l2.next;
    }

    ans = ans.sort((a,b)=>b-a);

    return makeList(ans);
};

function makeList(arr){
   return arr.reduce((Listnode, value, index, _arr)=>{
       let temp = new ListNode(value);
       if(index != 0){
           temp.next = Listnode;
       }
       return temp;
   }, null);
}
