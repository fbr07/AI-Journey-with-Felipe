#  Group Anagrams

""" Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""


def groupAnagrams(strs):

    #  I need to create a dictionary that will return the anagrams. A dictionary has a key (left) & value (right)
    # The key for this dictionary will be the occurrencesLettersCount and the value will be the words that you can create with those occurrencesLettersCount

    anagrams = {}

    # How would I know how many times a letter appears, how would I code that?
    """Well I can create a dictionary and it will contain all the lowercase letters of the alphabet and if that letter in that word is in the alphabet it will +1 that way
    we can keep track of the letter count for each word in strs"""
    """Since they letter count has to be unique to only that word in strs, this means that after we are done iterating through a word in strs the letter count must start from
    0 again and then count the letter occurrences of that new word that is iterating"""

    # I need to iterate trough all of the words in strs,
    # Then I need to iterate through all of the letters in that word so I can count the letter

    # I need to create a for loop that will iterate through all of the words in strs

    # Create another for loop that will then iterate through the letters of that word so I can count the occurences

    for word in strs:

        """Now I can create a dictionary that for key will have the lowercase alphabet and for value will have 0 for starting value and will be +1 for every letter that
        appears in that word"""
        """The reason we initialize this dictionary innside this for loop is becuase this dictionary will only have the information for that word that we are currently iterating.
        If we were to have this dictionary initialize not in this loop then it will record through all of the letters counts of all of the iteration of words in strs,
        and that is not what we want because we only want to create anagrams based on the count of that word so that count can only be for that word.
        So by having inside this loop it means when we iterate and we are on that word of strs, that count will only be for that word and once we are done
        iterating throught that word and we go onto the next word in strs, then the dictionary count starts at 0 for the letter occurences and +1 to whatever letter is 
        in that word"""

        countOfLetters = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
            "m": 0,
            "n": 0,
            "o": 0,
            "p": 0,
            "q": 0,
            "r": 0,
            "s": 0,
            "t": 0,
            "u": 0,
            "v": 0,
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0,
        }

        for letter in word:
            if letter in countOfLetters:
                countOfLetters[letter] += 1

        # Once we are done counting the letters of that word we must now add that count onto the dictionary anagrams
        """But since we are dealing with strings and strings are immutable but dictionaries are mutable. We must turn how many times a letter occur which is the value in
        countOfLetters to mutable because we will be using that and it will be our key for our anagrams dictionary"""
        # We can do this by using the tuple built-in Python method

        countOfLetterTuple = tuple(countOfLetters.values())

        """Since the value of countOfLetterTuple is the occurrences of the letters of that word in strs. And we know we will be using this to letter occurrences
        to be able to create anagrams based on those letter occurrences. Which means that the letter occurences which is the value in countOfLetters will not become the key 
        in anagram and the value will be anagram words based on letter occurrences (key)"""

        """So how do we add occurences of letters for that word, well we need to append the letter occurences to the dictionary anagrams, so we can say if those letter occurrences
        in countOfTuple is not in anagram then we append them
        """
        if countOfLetterTuple not in anagrams:
            anagrams[countOfLetterTuple] = []
            """In the above code we are saying that in anagram the key will be the letter occurences of countOfLetterTuple and the value will be a list of anagram words based on
            the letter occurences so we create an empty list [] so we can append that word into anagram which will be the value"""
        anagrams[countOfLetterTuple].append(word)

        # Once we are done iterating through that word we move onto the next one

    """Now that we are done iterating though all of the words in strs, we must not return the anagram words that were created based on the letter occurences
    we were able to use those letters to create words from that and we can find those words in value of anagrams dictionary so we return the values of anagrams"""
    return list(anagrams.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
