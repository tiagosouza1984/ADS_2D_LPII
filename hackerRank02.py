# n = int(input())
arr = [9,8,7,6,5]
arr.sort()
print(arr)
for i in range(len(arr)):
    if arr[i] > arr[i-1] and arr[i] == max(arr):
        print(arr[i-1])
        break
