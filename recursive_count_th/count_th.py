'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # The word must contain at least 2 characters to be able to meet the criteria. This will be used as our base case as we move through the word.
    if len(word) < 2:
        return 0
    else:
        # If th is the first 2 characters in the word, +1 and then remove the first character from the word and run again to check the next 2 characters.
        # Using the slice method object notation, we can take a slice of the first 2 characters in the string by setting the slice to stop at the 3rd character (index = 2)
        if word[:2] == 'th':
            return count_th(word[1:]) + 1
        # If th is not the first 2 characters in the word, remove the first character from the string and run again.
        # This continues until the length of the string is less than 2 (our base case).
        else:
            return count_th(word[1:])
