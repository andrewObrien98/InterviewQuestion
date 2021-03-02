"""
Given a string, find the length of the longest substring without repeating characters.
answer in this case should be abcdefghij
"""
class Solution:
  def lengthOfLongestSubstring(self, s):
    count = 0
    previous = "z"
    for i in s:
        if ord(i) - ord(previous) == 1:
            count += 1
        previous = i
    return count

print (Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10