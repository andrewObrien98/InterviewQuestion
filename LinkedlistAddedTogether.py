class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
      if l1.next == None:
          value = l1.val + l2.val
          if c > 9:
              value += 1
          l1.val = value % 10
          return l1
      l1.next = self.addTwoNumbers(l1.next, l2.next, l1.val + l2.val)
      value = l1.val + l2.val
      if c > 9:
          value += 1
      l1.val = value % 10
      return l1
    # Fill this in.

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val)
  result = result.next
# 7 0 8