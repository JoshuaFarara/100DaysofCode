'''
Find largest element in an array Using Native Approach
To find the largest element in an array, iterate over each element and compare it with the current largest element. 
If an element is greater, update the largest element. At the end of the iteration, the largest element will be found.
'''

def largest(arr, n):
    max = arr[0]

    for i in range(0, n):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [9, 12, 36, 27, 18, 50]
n = len(arr)
ans = largest(arr, n)
print("Largest in given array: ", ans)

# Using built-in function max()
def builtLargest(arr, n):
    Ans = max(arr)
    return Ans

arr2 = [9, 5, 6, 7, 8, 25]
theMax = builtLargest(arr2, n)
print("The max is: ", theMax)
