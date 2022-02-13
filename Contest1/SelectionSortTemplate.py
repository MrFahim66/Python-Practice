def SelectionSort(nums):
    for i in range(len(nums)):
        minpos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)


print('Enter array length:')
length = int(input())

for i in range(0, length):
    element = int(input().split())

print(numbers)
print()
SelectionSort(numbers)