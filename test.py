def smaller(arr):
    result = []
    for i in range(len(arr)):
        count = sum(1 for j in arr[i+1:] if j < arr[i])
        result.append(count)
    return result

print(smaller([5,4,2,1]))  # Output: [3, 2, 1, 0]