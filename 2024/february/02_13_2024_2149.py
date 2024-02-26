
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        results = [0] * len(nums)
        insert_positive, insert_negative = 0, 1
        for index in range(len(nums)):
            if nums[index] > 0:
                results[insert_positive] = nums[index]
                insert_positive += 2
            else:
                results[insert_negative] = nums[index]
                insert_negative += 2
        return results
