def majorityElement(nums):
    hashMap = {}
    n = len(nums)
    majorElement = n // 2
    for number in nums:
        if number in hashMap:
            hashMap[number] += 1
        else:
            hashMap[number] = 1

    if hashMap[number] > majorElement:
        return number


print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
