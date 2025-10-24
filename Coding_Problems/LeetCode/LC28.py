# 28. Find the Index of the First Occurrence in a String
""" Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack
Input: "sadbutsad" , needle="sad" 
"sad" occurs at index 0, so we return 0
"""


def firstIndexOccurrence(haystack, needle):
    for i in range(0, len(haystack) - len(needle) + 1):
        # haystack = sadbutsad needle=sad == 9 - 3 + 1) == 6 + 1 = 7 **remember we go from left to right so we first subtract len(haystack) - len(needle) then we + 1
        # for i in range(0, 7) *remember for range and slicing we start at start and we end 1 before the end. so our stopping will be index 6
        # so our indexes that we will be iterating trough are from 0:4 s=0,a=1,d=2,b=3,u=4,t=5,s=6 STOP

        if haystack[i : i + len(needle)] == needle:
            # slicing is the same as range meaning we start at start but we end 1 before the end, so our stopping will be index 2
            # so we are saying from haystack[0:3] *remember we stop 1 before so index 2
            # s=0 a=1 d =2 stop == sad  ** it does so therefore we return i becuase that will be our first occurence
            return i

    return -1


print(firstIndexOccurrence("sadbutsad", "sad"))
