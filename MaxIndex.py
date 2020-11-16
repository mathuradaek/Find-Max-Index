
arr = [1,2,1,3,5,6,4]
max_ele = arr[0]
count, index = 0, 0
for i in range(1, len(arr)):
    count += 1
    if arr[i] > max_ele:
        max_ele = arr[i]
        index = count
print('Position of Maximum Value in the list', arr, 'is', index)