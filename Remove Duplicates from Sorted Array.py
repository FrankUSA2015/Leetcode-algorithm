# -*- coding: utf-8 -*-
#题目：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
#解题思路：
#这个题利用了指针的方法，把下标作为指针。
class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums)==0:
            return 0
        else:
            i=0
            for j in range(1,len(nums)):
                if nums[i]!=nums[j]:
                    i=i+1
                    nums[i] = nums[j]
            return i+1