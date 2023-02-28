class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        li = [c + extraCandies >= max(candies) for c in candies]
        return li
    
obj = Solution()
candies = [int(x) for x in input().split()]
extraCandies = int(input())
print(obj.kidsWithCandies(candies, extraCandies))