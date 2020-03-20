# -*- coding: utf-8 -*-
#题目见：https://leetcode-cn.com/problems/valid-parentheses/
#解答思路：
# https://leetcode-cn.com/problems/valid-parentheses/solution/zhu-bu-fen-xi-tu-jie-zhan-zhan-shi-zui-biao-zhun-d/
#解法：
# 利用入栈和出栈的方法，实现对括号的比较。
#学到的知识：
# 可以利用list来模拟栈，出栈用list自带的函数pop()，入栈用append()
# i in str_dict，可以判断i这个关键词是否在字典中。
class Solution:
    def isValid(self, s) -> bool:
        stack = []
        str_dict = {")":"(","]":"[","}":"{"}
        for i in s:
            if stack and (i in str_dict):
                if str_dict[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if len(stack)==0:
            return True
        else:
            return False
nn = Solution()
cc = "([)]"
print(nn.isValid(cc))