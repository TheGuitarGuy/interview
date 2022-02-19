def oddOneOut(nums):
    nums.sort()
    n = max(nums)
    for i in range(n+1):
        if i != nums[i]:
            return i

print(oddOneOut([7,0,1,3,4,5,6,2, 8, 9, 10, 13] ))