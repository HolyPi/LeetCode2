def removeElement(nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)
        
nums = [1, 2, 2, 4, 1]
val = 1

print(removeElement(nums, val))
