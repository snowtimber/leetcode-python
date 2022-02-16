class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}
        for i, v in enumerate(nums):
            compliment = target - v
            if compliment in hashmap:
                return [hashmap[compliment], i]
            hashmap[v] = i
