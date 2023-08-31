'''
Day Tweny-Fourth of 100 Days of Code

June 24th, 2023

Todays program will merge two sorted arrays into a single sorted array.

# Todays Schedule

Merge Two Sorted Arrays
Subarray with given sum
Find duplicates in an array
Missing number in an array
Array Rotation

'''

# Merge Two Sorted Arrays
# Input: arr1[] = { 1, 3, 4, 5}, arr2[] = {2, 4, 6, 8} 
# Output: arr3[] = {1, 2, 3, 4, 4, 5, 6, 8}

import array as arr

def mergeArrays(stats, stats1, n, n1, statsMerge):
    i = 0
    j = 0
    k = 0

    while(i<n):
        stats3[k] = stats[i]
        k += 1
        i += 1

    while(j<n1):
        stats3[k] = stats1[j]
        k += 1
        j += 1

    stats3.sort()


stats = arr.array('i', [8, 6, 4, 2])
n=(len(stats))

stats1 = arr.array('i', [9, 7, 5, 3])
n1=(len(stats1))
print(stats, stats1)

stats3 = [0 for i in range(n+n1)]
mergeArrays(stats, stats1, n, n1, stats3)

print("Array after merging")
for i in range(n + n1):
    print(stats3[i], end=" ")

