class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict1 = {}
        for i in nums:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        sorted_items = sorted(dict1.items(), key=lambda item: item[1],  reverse=True)
        return [num for num, count in sorted_items[:k]]
        
        
        
        
        
        
        
        
        #Okay so currently Im thinking of adding every number in a dict then recording thier numbers of occurence, this should be o(n) but memory is also o(n) or maybe even more

