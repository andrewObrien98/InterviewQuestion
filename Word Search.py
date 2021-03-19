"""
Hi, here's your problem today. This problem was recently asked by Amazon:

You are given a 2D array of characters, and a target string. Return whether or not the word target word exists in the matrix. Unlike a standard word search, the word must be either going left-to-right, or top-to-bottom in the matrix.

Example:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

Given this matrix, and the target word FOAM, you should return true, as it can be found going up-to-down in the first column.

Here's the function signature:
"""


def word_search(matrix, word):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == word[0]:
                return findOtherLetters(matrix, row, col, word, len(word), 0)
    return False

def findOtherLetters(matrix, row, col, word, wordLength, iteration):
    if iteration == wordLength:
        return True
    if row < 0 or row > 3:
        return False
    if col < 0 or col > 3:
        return False
    if matrix[row][col] == word[iteration]:
        if findOtherLetters(matrix, row, col - 1, word, wordLength, iteration + 1):
            return True
        if findOtherLetters(matrix, row, col + 1, word, wordLength, iteration + 1):
            return True
        if findOtherLetters(matrix, row + 1, col - 1, word, wordLength, iteration + 1):
            return True
        if findOtherLetters(matrix, row + 1, col, word, wordLength, iteration + 1):
            return True
        if findOtherLetters(matrix, row + 1, col + 1, word, wordLength, iteration + 1):
            return True
        if findOtherLetters(matrix, row - 1, col - 1, word, wordLength, iteration + 1):
            return True
        if findOtherLetters(matrix, row - 1, col, word, wordLength, iteration + 1):
            return True
        if findOtherLetters(matrix, row - 1, col + 1, word, wordLength, iteration + 1):
            return True

    return False


# Fill this in.

matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']]
print(word_search(matrix, 'MASS'))


# True