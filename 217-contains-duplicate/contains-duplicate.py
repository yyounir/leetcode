'''
1. Understand
- Inputs a list of int nums
- Outputs a boolean
- Check to see whether a list has a duplicate
- Only output false if the element is distinct
- Only output true if the element has a duplicate
- Possible Edge Cases:
    - Empty list
    - One number in list

2. Plan


3. Implement
'''

class Solution:
    def containsDuplicate(self, nums):
        count = {}

        for i in range(len(nums)):
            if(nums[i] in count):
                count.update({nums[i] : count.get(nums[i])+ 1})
            else:
                count.update({nums[i] : 1})

        for value in count.values():
            if(value > 1):
                return True
        return False
        