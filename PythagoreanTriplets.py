"""
Hi, here's your problem today. This problem was recently asked by Uber:

Given a list of numbers, find if there exists a pythagorean triplet in that list. A pythagorean triplet is 3 variables a, b, c where a2 + b2 = c2

Example:
Input: [3, 5, 12, 5, 13]
Output: True
Here, 5^2 + 12^2 = 13^2.
"""
class Hash:
    def __init__(self):
        #create list
        self.list = []
        for i in range(50):
            self.list.append(0)

    def hash(self, number):#for this case I will just do a an easy one
        return number % 49

    def insert(self, number):
        index = self.hash(number * number)
        self.list[index] = number * number

    def find(self, number):
        index = self.hash(number)
        return self.list[index]

def findPythagoreanTriplets(nums):#first idea that came to my head, Brute force, will look for better solution
    for number in nums:
        cSquared = number * number
        for i in range(len(nums)):
            if nums[i] != number and i < len(nums) - 1:
               for j in range(i + 1,len(nums)):
                   if(nums[j] != number):
                        aSqaured = nums[i] * nums[i]
                        bSqaured = nums[j] * nums[j]
                        if aSqaured + bSqaured == cSquared:
                            return str(aSqaured) + " + " + str(bSqaured) + " = " + str(cSquared)

def simplerSolution(nums):#if I use a hash list I can simplify it
    hash = Hash()
    for number in nums:
        hash.insert(number)
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums) - 1):# could make it range(i + 1, len(nums) - 1)
            aSquared = nums[i] * nums[i]
            bSquared = nums[j] * nums[j]
            if(hash.find(aSquared + bSquared) == aSquared + bSquared):
                return str(aSquared) + " + " + str(bSquared) + " = " + str(hash.find(aSquared + bSquared))

list = [3, 12, 5, 13, 11]
print(findPythagoreanTriplets(list))
print(simplerSolution(list))
# True

