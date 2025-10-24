# Q: Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.


def isAnagram(s, t):
    """We need to be able to store each letter in string s & t, that way we know what letter they have and also the occurrences of the letters. We can create a hash map
    for s and t. That will store the letters of s & t and will have the occurrences as well. The key will be the letter and value will be the occurrence of that letter
    """

    sHashMap = {}
    tHashMap = {}

    # Then we have to create a for loop that will iterate through s and t.

    for sLetter in s:
        if sLetter in sHashMap:
            sHashMap[sLetter] += 1

        else:
            sHashMap[sLetter] = 1

    for tLetter in t:
        if tLetter in tHashMap:
            tHashMap[tLetter] += 1

        else:
            tHashMap[tLetter] = 1

    """Okay so now that we have store our letter and occurrences in hash map for s and t. We now that so far are key is the letter and our value is the occurrences count.
    So if the sHashMap == tHashmap then this means that they are anagram. How do we obtain the values of sHashMap and tHashMap? """

    """Well we know that dictionaries in Python are equal if and only if they have the same sets of keys and each key has the same corresponding value.
    If I have sHashMap == tHashMap, Python is checking each key-value pair in both hash maps"""

    if sHashMap == tHashMap:
        return True

    else:
        return False


print(isAnagram("racecar", "carrace"))
