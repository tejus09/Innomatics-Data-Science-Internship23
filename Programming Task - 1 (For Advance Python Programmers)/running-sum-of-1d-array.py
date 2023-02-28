class Solution:
    def runningSum(self, nums):
        #Lets assume the current sum to be 0
        curr_sum = 0

        #Lets create a temp. list which is to be returned in end
        temp_list=[]

        #Traverse the nums
        for i in range(len(nums)):
            curr_sum = curr_sum + nums[i]
            temp_list.append(curr_sum)
        #Return the temp_list
        return temp_list

li = [int(x) for x in input().split()]
sol = Solution()
print(sol.runningSum(li))
    