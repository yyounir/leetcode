class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pointer1 = 0
        pointer2 = 1

        while not pointer1 == len(nums):
            if(nums[pointer1] + nums[pointer2] == target):
                return [pointer1 , pointer2]
            else:
                pointer2 += 1
            if(pointer2 == len(nums)):
                pointer1 += 1
                pointer2 = pointer1 + 1
        return [-1]

