class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = {}

        for i in range(len(nums)):
            if nums[i] in count:
                count.update({nums[i] : count.get(nums[i]) + 1 })
            else:
                count.update({nums[i] : 1})
        
        for key in count:
            while(count.get(key) > 1):
                nums.remove(key)
                count.update({key : count.get(key) - 1})

        # return nums
        