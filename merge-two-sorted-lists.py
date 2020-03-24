# -*- coding: utf-8 -*-
# Definition for singly-linked list.
#题目：21题
# https://leetcode-cn.com/problems/merge-two-sorted-lists/
#结题方法：用到了递归的方法找到
#具体解法见：
#https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/he-bing-liang-ge-you-xu-lian-biao-by-leetcode/
#学到：
#（1）合并链表。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next =  self.mergeTwoLists(l1,l2.next)
            return l2

