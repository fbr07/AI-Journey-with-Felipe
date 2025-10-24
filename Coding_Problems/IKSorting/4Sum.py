def fourSum(arr, target):
    arr.sort()
    quadruples = []

    """Notice how above for if statement the pointer has to be greater than its starting point because if our pointer is
        greater than its starting point it ensures that there is a previous element to compare it with"""

    """Why do we compare our current value to its previous value? Because if the current value == its previous value, that 
        means that the current value is a duplicate so therefore we have to skip the current element"""

    """ What are we using continue? What continue does is skips every code below it, every code that is in the loop it skips
        it and then goes back to the loop. So we use it because if our current value is a duplicate we then move the pointer so
        now i has a new value so we use continue to skip all the code below and we have to make sure that our new current i is not
        a duplicate so we can move forward with our rest of our code, is it is another duplicate then we move to right and then
        continue and go back to the for and if statement"""
    for i in range(len(arr) - 3):
        if i > 0 and arr[i] == arr[i - 1]:
            continue  # Skip duplicates for `i`

        for j in range(i + 1, len(arr) - 2):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue  # Skip duplicates for `j`

            k = j + 1
            z = len(arr) - 1

            while k < z:
                total_sum = arr[i] + arr[j] + arr[k] + arr[z]

                if total_sum == target:
                    quadruples.append([arr[i], arr[j], arr[k], arr[z]])

                    # Skip duplicates for `k`
                    while k < z and arr[k] == arr[k + 1]:
                        k += 1

                    # Skip duplicates for `z`
                    while k < z and arr[z] == arr[z - 1]:
                        z -= 1

                    # Move both pointers after processing duplicates
                    k += 1
                    z -= 1
                elif total_sum < target:
                    k += 1
                else:
                    z -= 1

    return quadruples


print(fourSum([2, 1, 6, 3, 1, 3, 5, 4, 4, 5, 6, 2], 11))
