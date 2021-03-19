"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

You have 2 integers n and m representing an n by m grid, determine the number of ways you can get from the top-left
to the bottom-right of the matrix y going only right or down.

Example:
n = 2, m = 2

This should return 2, since the only possible routes are:
Right, down
Down, right.

Here's the signature:
"""
def num_ways(n, m):#this is my first idea
    return 1 + numWays(1,1,n,m)
#the way that I will try to look at this is that everthing is falling down and that each time we shift to the right we count it as a variation.
#the only rules we have to add is that once it either reaches the col count or row count we return 0
def numWays(curRow, curCol, maxRow, maxCol):
    if curCol >= maxCol:
        return 0
    if curRow >= maxRow:
        return 0
    return numWays(curRow + 1, curCol, maxRow, maxCol) + 1 + numWays(curRow, curCol + 1, maxRow, maxCol)
  # Fill this in.

def bestSolution(m,n):
    #here we will just use the mathmatical formula to find it
    path = 1
    for i in range(n, (m + n - 1)):
        path *= i
        path//= i - n + 1
    return path

print(num_ways(3,3))
print(bestSolution(3,3))
# 2
