def k_most_frequent(k, words):
    wordCount = {}
    for word in words:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1

    # Step 2: Convert dictionary to list of (word, occurrences) tuples
    wordCountTuple = list(wordCount.items())

    # Step 3: Sort the list of tuples lexicographically by word first
    wordCountTuple.sort(key=lambda wordsKeyCountValue: wordsKeyCountValue[0])

    # Step 4: Then sort the list of tuples by occurrences in descending order
    wordCountTuple.sort(
        key=lambda wordsKeyCountValue: wordsKeyCountValue[1], reverse=True
    )

    # Step 5: Get the top `k` frequent words
    kNumberFrequentWords = wordCountTuple[:k]

    # Step 6: Extract just the words from the sorted list of tuples
    mostFrequentWords = [
        wordsKeyCountValue[0:] for wordsKeyCountValue, _ in kNumberFrequentWords
    ]

    return mostFrequentWords


print(
    k_most_frequent(
        4,
        [
            "car",
            "bus",
            "taxi",
            "car",
            "driver",
            "candy",
            "race",
            "car",
            "driver",
            "fare",
            "taxi",
        ],
    )
)
