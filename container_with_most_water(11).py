"""You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water."""

def maxArea(height):
    maxArea = -1
    l, r = 0, len(height)-1

    while l < r:
        currArea = (r - l) * min(height[l], height[r])
        maxArea = max(maxArea, currArea)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return maxArea

print(maxArea([1,8,6,2,5,4,8,3,7]))