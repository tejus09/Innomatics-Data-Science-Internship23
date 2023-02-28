class Solution(object):
    def shuffle(self, nums, n):
        #find mid index
        mid = len(nums)//2

        #splitting list
        li1 = nums[:mid]
        li2 = nums[mid:]

        #Temp list
        li = []
        for i in range(len(li1)):
            li.append(li1[i])
            li.append(li2[i])
            
        #return the temp list
        return li
    
obj = Solution()
nums = [int(x) for x in input().split()]
n = int(input())
print(obj.shuffle(nums, n))