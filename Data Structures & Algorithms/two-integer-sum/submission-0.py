class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        database = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in database:
                return [database[rem], i]
            database[nums[i]] = i
