# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append
# the additional letters onto the end of the merged string. Return the merged string.
# ex: Input: word1 = "ab", word2 = "pqrs"  --> Output: apbqrs"


def mergerAlternatively(word1, word2):
    # Since we have two arguments in our function. I need to create 2 pointers, one for each argument
    i = 0
    j = 0

    # I will also create a new variable call mergeString where it will contain the merging
    mergeString = ""

    # I am going to create a while loop that will say as long as word1 and word2 have letters we will merge the strings alternatively.
    # If either word1 or word2 have no more letters then this look will break since we'll not be able to add letters alternatively

    while i < len(word1) and j < len(word2):
        # what this is saying is as long as i & j are less than the length of the words loop continues, if not then it breaks
        mergeString += word1[i]
        i += 1
        mergeString += word2[j]
        j += 1

    # Append any remaining elements
    if i < len(word1):
        mergeString += word1[i:]
        # Add remaining elements of word1 to merged list
    if j < len(word2):
        mergeString += word2[j:]
        # Add remaining elements of word2 to merged list

    return mergeString


print(mergerAlternatively("abcd", "pq"))
