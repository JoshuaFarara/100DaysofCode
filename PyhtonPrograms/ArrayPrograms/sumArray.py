# progrma to find the sum of an array

arr = [20, 20, 20, 20, 20, 5]

def sumArray(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

total = sumArray(arr)
print(total)

ans = sum(arr)
print(ans)