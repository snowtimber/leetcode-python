class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        three_sum = []

        #initiate dictionaries
        #create hash map for compliment of 2 numbers
        compliment = {}

        #dict to make sure result is unique
        existing = {}

        if len(nums) < 3:
            return []
        elif nums == [0,0,0]:
            return [[0,0,0]]

        #add up all 2 numbers and create a hash map for remaining compliment
        for i,x in enumerate(nums):

            for j,y in enumerate(nums):
                if i>=j:
                    continue

                #find compliment z to x + y
                z = -x-y
                #if compliment exits in dictionary, add to result list.
                if y in compliment:

                    #ensure unique 3sum values by using dict
                    a, b, j_prev = compliment[y]
                    three = sorted([a,b,y])

                    if str(three) not in existing and j != j_prev:
                        three_sum.append(three)
                        existing[str(three)] = 0
                        #print(f"x = {x}, y = {y}, z = {z}, i = {i}, j = {j} {three}")
                #add compliment to dictionary
                #key = compliment value = original numbers in list
                compliment[z] = x,y,j
                #print(f"x = {x}, y = {y}, z = {z}, i = {i}, j = {j}")

        if set(nums) == [0]:
            return [[0,0,0]]
        return three_sum
                    
