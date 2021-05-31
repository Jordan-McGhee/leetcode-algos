"""

#1221
Split a String Into Balanced Strings

Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.

Example:
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.


"""

def balancedStringSplit(s):
    # we need two variables, one to return the total number of balances, and the second, a variable we will change depending on if if the character we iterate over is an L or an R
    total = 0
    balance = 0

    # iterate over every character
    for char in s:
        # if the character is an L, we'll subtract 1 from balance
        if char == "L":
            balance -= 1

            # if balance == 0, we'll increment total. This means that there would have to be as many Rs as Ls to bring the balance back down to zero. 
            if balance == 0:
                total += 1

        # do the same thing for R, except we increment balance instead of subtracting 1
        if char == "R":
            balance += 1
            if balance == 0:
                total += 1

    return total

# print(balancedStringSplit("RLRRLLRLRL"))

"""

#1832
Check if the Sentence is Pangram

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Example:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

"""

def pangramCheck(sentence):
    # establish variable with all letters in alphabet
    alpha = "abcdefghijklmnopqrstuvwxyz"

    # iterate over every character in alpha
    for char in alpha:
        # if char in sentence, continue to next char
        if char in sentence:
            continue

        # else, return False and stop loop
        else:
            return False

    return True

print(pangramCheck("thequickbrownfoxjumpsoverthelazydog"))