# -*- coding: utf-8 -*-
#题目 https://leetcode-cn.com/problems/longest-common-prefix/
#结题思路：
#https://leetcode-cn.com/problems/longest-common-prefix/solution/python-shui-ping-sao-miao-fa-by-huamei/
#学到的知识：
#字符串类型自带了find函数，可以用来查找某一个字符是否在要找的字符里
#这里用到了在多个字符的找共同点的时候，实际上是两两之间进行比较，只要所有的字符都有共同的一块，那就一定有相同的。
class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ""
        s=strs[0]
        for i in range(1,len(strs)):
            while strs[i].find(s) != 0:
                s=s[:-1]
        return s

nn = Solution()
cc = ["flower","flow","flight"]
print(nn.longestCommonPrefix(cc))