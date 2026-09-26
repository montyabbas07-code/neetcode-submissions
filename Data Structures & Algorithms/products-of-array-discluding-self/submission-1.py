class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num = 1
        num2 = 1
        zeros = 0
        for i in nums:
            if i == 0:
                num*= i 
                zeros +=1
                continue
            num *= i
            num2 *= i

        list1 = []
        for i in range(len(nums)):
            if nums[i] == 0 and zeros > 1:
                list1.append(0)
                continue 
            elif nums[i] == 0:
                list1.append(num2)
                continue
            list1.append(num//nums[i])
        return list1