def ContainsNearbyDuplicate(nums, k):
	for i in range(len(nums)):
		print("i=%d" % i)
		for j in range(i+1, i+k+1):
			print("  j=%d" % j)
			if j >= len(nums):
				return False
				break
			if nums[i] == nums[j]:
				return True
				break
	else:
		return False

a = [1,2,3,4,2,3,5]
print(ContainsNearbyDuplicate(a, 3))