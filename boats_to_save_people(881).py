"""You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit.
Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit."""

def numRescueBoats(people,limit):
    people.sort()
    l, r = 0, len(people) - 1
    res = 0
    while l <= r:
        remain = limit - people[r]
        r -= 1
        res += 1
        if l <= r and remain >= people[l]:
            l += 1

    return res

print(numRescueBoats([3,5,3,4],5))