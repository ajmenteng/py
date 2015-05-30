def containsDuplicate(nums):
    counter = {}
    i = 0
    while counter.get(nums[i],0) < 2:
        counter[nums[i]] = counter.get(nums[i],0) + 1
        i += 1
    if i == len(nums)-1:
        return False
    else:
        return True

print(containsDuplicate([1,2,3,4,2,5,3]))