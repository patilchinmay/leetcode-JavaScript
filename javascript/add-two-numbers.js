// https://leetcode.com/problems/add-two-numbers/
// https://leetcode.com/submissions/detail/269793865/

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

var addTwoNumbers = function(l1, l2) {
    let first = parseListNode(l1);
    let second = parseListNode(l2);

    first = BigInt(first.reverse().join(''));
    second = BigInt(second.reverse().join(''));

    let ans = BigInt(first + second).toString().split('').map(digit => Number(digit));

    let listNode = makeList(ans);

    return listNode;
};

function parseListNode(node) {
    let ans = [];

    do{
        ans.push(node.val);
        node = node.next;
    }while(node != null);

    return ans;
}

function makeList(arr){
   return arr.reduce((Listnode, value, index, _arr)=>{
       let temp = new ListNode(value);
       if(index != 0){
           temp.next = Listnode;
       }
       return temp;
   }, new ListNode(0));
}
