# class Solution:
#     def findTheArrayConcVal(self, nums: List[int]) -> int:
#         ans=0
#         if len(nums)%2==1:
#             ans=nums[len(nums)//2]
#         for i in range(len(nums)//2):
#             ans+=int(str(nums[i])+str(nums[len(nums)-1-i]))
#         return ans

# # .....................................................................................................

# class Solution:
#     def minimumSum(self, num: int) -> int:
#         num = str(num)
#         num = sorted(num)
#         st1 = ""
#         st2 = ""
#         st1 += num[1]+num[3]
#         st2 += num[0]+num[2]
#         sum = int(st1)+int(st2)
#         return sum    

# # .......................................................................................................
    
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         n = str(n)
#         m = 0
#         while m != 1 and m != 4:
#             m = sum(int(i)**2 for i in n)
#             n = str(m)
#         if m == 1:
#             return True
#         else: 
#             return False
        
# # ...........................................................................................................
    
# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         if len(set(nums)) == len(nums):
#             return False
#         for i in range(len(nums)):
#             if len(nums[i:i+k+1]) != len(set(nums[i:i+k+1])):
#                 return True
#         return False
        
# # ...............................................................................................................
    
# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         lst = []
#         nums1 = nums[:n]
#         nums2 = nums[n:]

#         # for i in range(len(nums1)):
#                 lst.append(nums1[i])
#                 lst.append(nums2[i])
#         return lst