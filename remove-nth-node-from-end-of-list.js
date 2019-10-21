// https://leetcode.com/problems/remove-nth-node-from-end-of-list/
// https://leetcode.com/submissions/detail/271904225/

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let ans = [];

    while(head != null){
        ans.unshift(head.val);
        head = head.next;
    }

    ans.splice(n-1, 1);

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
