   

# class Solution(object):
    
#     def isHappy(self, n):
#         num = []
#         num = splitIntoArray(n)
#         while sumsquare(num) != 1:
#             n = sumsquare(num)
#             num = splitIntoArray(n)

#         return True      
      

 

# def sumsquare(numdigits):
#     sumdigits = 0
#     for i in range(len(numdigits)):
#         sumdigits += numdigits[i] ** 2
#     return sumdigits



# def splitIntoArray(num):
#     numdigits = [int(i) for i in str(num)]
#     return numdigits
#****************************************
#HAPPY NUMBER
#Input: 19
#Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
class Solution(object):
    
    def isHappy(self, n):
        
        s = {1}
        while n not in s:
            s.add(n)
            n = sumsquare(n)
            

        return n == 1      



def sumsquare(n):
    n = sum(i * i for i in map(int, str(n)))
    
    return n

    

