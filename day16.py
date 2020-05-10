# Given a string containing only three types of characters: '(', ')' and '*', 
# write a function to check whether this string is valid. We define the validity of a string by these rules:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.

# def checkValidString( s):
#     """
#     :type s: str
#     :rtype: bool
#     """
#     for i in s:
#         if i != "(" or i != ")" or i != "*":
#             return False
#     for i in s:
#         if i =="*":
#             s.replace(i,"(") or s.replace(i,")") or s.replace(i,"")
#     for i in s:
#         if i == "(" and ")" in s:
#             if s.index("(") < s.index(")"):
#                 return True
#             else:
#                 return False

# def checkValidString(s):

#     # if s == "":
#     #     return True
#     # allowed = ["(",")","*"]
#     # for i in s:
#     #     if i not in allowed:
#     #         return False
#     # if "(" in s and ")" not in s:
#     #     return False
#     # if  ")" in s and "(" not in s:
#     #     return False
#     # if "(" in s and ")" in s:
#     #     for i in s:
#     #         if s.index("(") < s.index(")"):
#     #             return True
#     #         else:
#     #             return False
#     if conditions(s) == True:
#         return True
#     elif conditions(s) == False and "*" not in s:
#         return False
#     else:
#         for i in s:
#             if i == "*":
#                 saved = s
#                 s.replace(i,"(")
#                 if conditions(s) == False:
#                     s = saved
#                     s.replace(i,")")
#                     if conditions(s) == False:
#                         s = saved
#                         s.replace(i,"")
#                         if conditions(s) == False:
#                             return False
#             return True
            
# def conditions(s):
#     if s == "":
#             return True
#     allowed = ["(",")","*"]
#     for i in s:
#         if i not in allowed:
#             return False
#     if "(" in s and ")" not in s:
#         return False
#     if  ")" in s and "(" not in s:
#         return False
#     if "(" in s and ")" in s:
#         for i in s:
#             if s.index("(") < s.index(")"):
#                 return True
#             else:
#                 return False

# SOLUTION 1
# def checkValidString(s):
#     if len(s)==0 or s == "*":
#         return True
#     if len(s) == 1:
#         return False

#     leftBalance = 0
#     for i in s:
#         if i == ')':
#             leftBalance-=1
#         else:
#             leftBalance+=1
#         if leftBalance < 0:
#             return False
#         elif leftBalance==0:
#             return True
#     rightBalance = 0
#     for i in reversed(s):
#         if i == "(":
#             rightBalance-= 1
#         else:
#             leftBalance+=1
#         if rightBalance < 0:
#             return False
#         #elif rightBalance==0:
#     return True
# SOLUTION 2
def checkValidString(s):
    stack,star_stack = [],[]
    for index,char in enumerate(s):
        if char=="(":
            stack.append(index)
        elif char=="*":
            star_stack.append(index)
        elif char==")":
            if len(stack)>0:
                stack.pop()
            elif len(star_stack)>0:
                star_stack.pop()
            else:
                return False
    while stack and star_stack:
        if stack[-1]<star_stack[-1]:
            stack.pop()
            star_stack.pop()
        else:
            break
    return len(stack)==0

print(checkValidString("("))
print(checkValidString(")"))
print(checkValidString("*()(())*()(()()((()(()()*)(*(())((((((((()*)(()(*)"))
print(checkValidString("(*)"))

            

    
