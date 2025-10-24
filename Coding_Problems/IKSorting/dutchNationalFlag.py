"""def dutchFlag(balls):
    bluePointer = -1
    redPointer = 0
    
    
    for i in range(0, len(balls)):
        if balls[i] == "R":
            balls[redPointer], balls[i] = balls[i], balls[redPointer]
            redPointer +=1
        
        elif balls[i] == "B":
            balls[bluePointer], balls[i] = balls[i], balls[bluePointer]
            bluePointer -=1
    return balls"""


def dutchFlag(balls):
    redIndex = 0
    blueIndex = len(balls) - 1  # Start at the end of the array
    greenPointer = 0

    while greenPointer <= blueIndex:
        if balls[greenPointer] == "R":
            # Swap the current element with the element at redIndex
            balls[redIndex], balls[greenPointer] = balls[greenPointer], balls[redIndex]
            redIndex += 1
            greenPointer += 1
        elif balls[greenPointer] == "G":
            greenPointer += 1
        elif balls[greenPointer] == "B":
            # Swap the current element with the element at blueIndex
            balls[greenPointer], balls[blueIndex] = (
                balls[blueIndex],
                balls[greenPointer],
            )
            blueIndex -= 1
            # Do not increment `currentIndex` here because the swapped element needs to be checked

    return balls


print(dutchFlag(["G", "B", "G", "G", "R", "B", "R", "G"]))
