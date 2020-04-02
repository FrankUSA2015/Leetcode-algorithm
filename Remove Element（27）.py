# -*- coding: utf-8 -*-
#题目：https://leetcode-cn.com/problems/remove-element/，
#题号：27移除元素
#知识：利用list自带的函数remove来实现删除相同的数据。要注意删除的过程中list的长度和位置都会改变。
class Solution:
    def removeElement(self, nums, val) -> int:
        len_data= len(nums)
        if len_data==0:
            return len_data
        else:
            same_num =0
            i=0
            j=0
            while i<len_data:
                if nums[i]==val :
                    nums.remove(val)
                    len_data=len(nums)
                    same_num = same_num+1
                else:
                    i=i+1
            return len_data

aa = Solution()
nums = [3,2,2,3]
val = 3
print(aa.removeElement(nums,val))