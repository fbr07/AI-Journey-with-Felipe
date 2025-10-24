def mergeIntoSecond(first, second):
    firstArrayPointer = len(first) - 1
    secondFirstHalf = len(first) - 1
    secondmergearray = len(second) - 1

    while firstArrayPointer >= 0 and secondFirstHalf >= 0:
        if first[firstArrayPointer] > second[secondFirstHalf]:
            second[secondmergearray] = first[firstArrayPointer]
            firstArrayPointer -= 1
            secondmergearray -= 1
        else:
            second[secondmergearray] = second[secondFirstHalf]
            secondFirstHalf -= 1
            secondmergearray -= 1

    while firstArrayPointer >= 0:
        second[secondmergearray] = first[firstArrayPointer]
        firstArrayPointer -= 1
        secondmergearray -= 1

    return second


print(mergeIntoSecond([1, 3, 5], [2, 4, 6, 0, 0, 0]))
