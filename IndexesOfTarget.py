"""
Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.

Example:
Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150
Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9
Output: [-1, -1]

"""

#My solution was to loop through the list
#for the first one that I find I set that index equal to first and then every one after that I set to last
class Solution:
    def getRange(self, arr, target):
        first = -1
        last = -1
        for i in range(len(arr)):
            if(arr[i] == target):
                if(first == -1):
                    first = i
                last = i
        return "[" + str(first) + "," + str(last) + "]"

#This recursive one is not needed and I know its a bit more complex but just thought it would be fun to do for the practice
    def getRangeRecursively(self, arr, target):
        return self.rangeRecursively(arr, target,0 ,-1, -1)

    def rangeRecursively(self, arr, target, index, first, last):
        if(index == len(arr)):
            return "[" + str(first) + "," + str(last) + "]"
        if (arr[index] == target):
            if (first == -1):
                return self.rangeRecursively(arr, target, index + 1, index, last)
            return self.rangeRecursively(arr, target, index + 1, first, index)
        return self.rangeRecursively(arr, target, index + 1, first, last)

# Fill this in.

# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(Solution().getRange(arr, x))
print(Solution().getRangeRecursively(arr, x))
# [1, 4]