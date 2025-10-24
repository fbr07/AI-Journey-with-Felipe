def threeSum(arr):
    """
    :type nums: List[int]
    :rtype: List[str]
    """

    arr.sort()
    triplets = []

    i = 0
    while i < len(arr) - 2:
        if i > 0 and arr[i] == arr[i - 1]:
            i += 1
            continue

        leftToRight = i + 1
        endToLeft = len(arr) - 1

        while leftToRight < endToLeft:
            total_sum = arr[i] + arr[leftToRight] + arr[endToLeft]

            if total_sum == 0:
                triplets.append(f"{arr[i]},{arr[leftToRight]},{arr[endToLeft]}")
                while (
                    leftToRight < endToLeft and arr[leftToRight] == arr[leftToRight + 1]
                ):
                    leftToRight += 1
                while leftToRight < endToLeft and arr[endToLeft] == arr[endToLeft - 1]:
                    endToLeft -= 1
                leftToRight += 1
                endToLeft -= 1
            elif total_sum < 0:
                leftToRight += 1
            else:
                endToLeft -= 1

        i += 1

    return triplets


print(threeSum([10, 3, -4, 1, -6, 9]))
