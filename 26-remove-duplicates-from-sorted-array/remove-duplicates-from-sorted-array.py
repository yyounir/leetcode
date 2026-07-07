'''
1. Understand
- Inputs a list of ints
- Outputs a list
- Remove duplicates from an array
- Possible edge cases:
    - Empty list
    - No duplicates

2. Plan
- Create a function
- Create a new dictionary called count, to keep track of the numbers
- Create a new variable named "newList" which keeps track of the updated list
- Create a new variable named "length" which is the length of the list
- Create a for loop to iterate through the loop via for each:
    - If the number is in the dictionary, update the value to two
    - Else: Update the dictionary to create a new key and set it equal to 1
- Create a for loop to iterate through the dictionary, and add each key to the new list
- Return the new list

3. Implement
'''

class Solution:
    def removeDuplicates(self, nums):
        pointer1 = 0
        pointer2 = 1

        for i in range(len(nums)-1):
            if(pointer2 != len(nums)):
                if(nums[pointer1] == nums[pointer2]):
                    nums.remove(nums[pointer2])
                    continue
                else:
                    pointer1 += 1
                    pointer2 += 1
            else:
                break

        print(nums)