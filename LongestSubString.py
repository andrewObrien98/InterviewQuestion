"""
Given a string, find the length of the longest substring without repeating characters.
"""
class Solution:
  def lengthOfLongestSubstring(self, s):
    list = s
    count = 0
    previous = "z"
    for i in list:
        if ord(i) - ord(previous) == 1:
            count += 1
        previous = i
    return count
    # Fill this in.

print (Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10