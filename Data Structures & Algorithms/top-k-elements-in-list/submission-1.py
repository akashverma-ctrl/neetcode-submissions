class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        
        max = 0
        for i in nums:
            d[i] = d.get(i, 0) + 1
            if i > max:
                max = i
        temp = [0]*(len(nums) + 1) if max < len(nums) else [0]*(max+1)

        for i, val in d.items():
            if temp[val]:
                temp[val].append(i)
            else:
                temp[val] = [i]

        result = []
        for i in temp[::-1]:
            if i:
                for j in i:
                    if k:
                        result.append(j)
                        k -= 1
        return result
        

        