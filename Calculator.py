"""
Hi, here's your problem today. This problem was recently asked by Google:

Given a mathematical expression with just single digits, plus signs, negative signs, and brackets, evaluate the expression. Assume the expression is properly formed.

Example:
Input: - ( 3 + ( 2 - 1 ) )
Output: -4
Here's the function signature:
"""
class Node:
    def __init__(self, element):
        self.right = None
        self.left = None
        self.element = element
def eval(expression):
    list = expression.split(" ")
    


def insert(element):
    print("hello")

  # Fill this in.

print(eval('- ( 3 + ( 2 - 1 ) )'))
# -4