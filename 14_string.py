# class Solution:
#     def percentageLetter(self, s: str, letter: str) -> int:
#         l = len(s)
#         count = 0
#         for i in s:
#             if i == letter:
#                 count+=1
#         return int(count/l*100)

# # .............................................................................................
    
# class Solution:
#     def minLength(self, s: str) -> int:
#         while('AB' in s or 'CD' in s):
#             if('AB' in s):
#                 s = s.replace('AB', '')
#             if('CD' in s):
#                 s = s.replace('CD', '')
#         return len(s)
        
# # ..............................................................................................
    
# class Solution:
#     def divideString(self, s: str, k: int, fill: str) -> List[str]:
#         res = []
#         for i in range(0, len(s), k):
#             l = s[i:i+k]
#             res.append(l + (k-len(l)) * fill)
#         return res