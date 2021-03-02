"""
Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate this using strings.

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

Example:
Input: "((()))"
Output: True

Input: "[()]{}"
Output: True

Input: "({[)]"
Output: False
"""

#this is my brute force solution
class Solution:
    def isValid(self, s):
        list = [0,0,0]
        for i in s:
            self.hash(i, list)
        for i in list:
            if(i != 0):
                return False
        return True

    # Fill this in.
    def hash(self, s, list):
        if s == ")":
            list[0] -= 1
        elif s == "(" and list[0] != -1:
            list[0] += 1
        if s == "}":
            list[1] -= 1
        elif s == "{" and list[1] != -1:
            list[1] += 1
        if s == "]" and list[2] != -1:
            list[2] -= 1
        elif s == "[":
            list[2] += 1

# Test Program
s = "()(){(())"
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))

s = ")))((("
# should return True
print(Solution().isValid(s))