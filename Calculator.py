"""
Hi, here's your problem today. This problem was recently asked by Google:

Given a mathematical expression with just single digits, plus signs, negative signs, and brackets, evaluate the expression. Assume the expression is properly formed.

Example:
Input: - ( 3 + ( 2 - 1 ) )
Output: -4
Here's the function signature:
"""
def eval(expression):
    listOfLeftBrackets = []
    listOfRightBrackets = []
    list = expression.split(" ")
    for i in range(len(list)):
        if(list[i] == "("):
            listOfLeftBrackets.append(i)
        elif (list[i] == ")"):
            listOfRightBrackets.append(i)
    if(len(listOfRightBrackets) != len(listOfLeftBrackets)):
        return "not pausible"
    number = 0
    size = len(listOfLeftBrackets)
    for i in range(size):
        startIndex = listOfLeftBrackets[size - i - 1]
        endIndex = listOfRightBrackets[i]
        negation = "+"
        for j in range(startIndex + 1, endIndex):
            print(list[j])
            if(list[j] == "-"):
                negation = "-"
            elif(list[j] == "-"):
                negation = "+"
            elif list[j].isdigit() and negation == "+":
                number += int(list[j])
                list[j] = 0
            elif list[j].isdigit() and negation == "-":
                number -= int(list[j])
                list[j] = 0
        list[startIndex] = 0
        list[endIndex] = 0

    return number



  # Fill this in.

print(eval('- ( 3 + ( 2 - 1 ) )'))
# -4