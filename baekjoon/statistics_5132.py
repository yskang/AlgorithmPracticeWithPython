# https://www.acmicpc.net/problem/2108
import sys
import math

def get_average(nums, offset, n):
    s = 0
    for i in range(len(nums)):
        s = s + (i - offset) * nums[i]
    return round(s/n)


def get_median(nums, offset, n):
    s = 0
    i = 0
    while True:
        s += nums[i]
        if s > math.floor(n/2):
            return i - offset
        i += 1


def get_most_frequent_number(nums, OFFSET):
    maxes = []
    max_count = 0

    for i in range(len(nums)):
        if max_count < nums[i]:
            max_count = nums[i]
            maxes = [i]
        elif max_count == nums[i]:
            maxes.append(i)

    if len(maxes) > 1:
        return sorted(maxes)[1] - OFFSET
    return maxes[0] - OFFSET


def get_range(nums, OFFSET):
    min = 0
    max = 0
    for i in range(len(nums)):
        if nums[i] > 0:
            min = i
            break
    for i in range(len(nums)-1, -1, -1):
        if nums[i] > 0:
            max = i
            break
    return max - min


if __name__ == "__main__":
    OFFSET = 4000
    nums = [0] * 8001
    N = int(input())
    n_map = {}

    for i in range(N):
        n = int(sys.stdin.readline())
        nums[n + OFFSET] += 1

    print(get_average(nums, OFFSET, N))
    print(get_median(nums, OFFSET, N))
    print(get_most_frequent_number(nums, OFFSET))
    print(get_range(nums, OFFSET))
