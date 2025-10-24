def groupAnagrams(strs):

    hashMap = {}
    for words in strs:
        if words in hashMap:
            hashMap[words] += 1

        else:
            hashMap[words] = 1

    print(hashMap)


print(strs(["act", "pots", "tops", "cat", "stop", "hat"]))
