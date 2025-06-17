def findKthPositive(arr, k):
    current = 1
    count = 0
    while count != k:
        if current in arr:
            current += 1
        else:
            current += 1
            count += 1
    return current - 1

# Можно лучше, решить в сложности O(n)
a = findKthPositive([2,3,4,7,11], 5)
b = findKthPositive([1,2,3,4], 2)
print(a, b)