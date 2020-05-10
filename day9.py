# def backspaceCompare(S, T):
#     """
#     :type S: str
#     :type T: str
#     :rtype: bool
#     """
#     #sum(i * i for i in map(int, str(n)))
#     newS = []
#     newT = []
#     newS = [char for char in S]
#     newT = [char for char in T]
#     print(newS)
#     print(newT)
#     for i in range(0,len(newS)-1):
#         if newS[i] == "#":
#             del newS[i-1:i+1]
#     for j in range(0,len(newT)-1):
#         if newT[j] == "#":
#             del newT[i-1:i+1]
#     print(newS)
#     print(newT)
#     sp = ""
#     S = sp.join(newS)
#     T = sp.join(newT)
#     if S == T:
#         return True
# 
#Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
   
def backspaceCompare( S: str, T: str) -> bool:
    S, T = _helper(S), _helper(T)
    return S == T

def _helper(s):
    while "#" in s:
        i = s.index("#")
        s = s[:i-1] + s[i+1:] if i > 0 else s[i+1:]
    return s
   

        
# for element in list:
#     result += str(element)
#     return result
print(backspaceCompare( "ab#c",  "ad#c"))
        
