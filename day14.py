# 1 <= s.length <= 100
# s only contains lower case English letters.
# 1 <= shift.length <= 100
# shift[i].length == 2
# 0 <= shift[i][0] <= 1
# 0 <= shift[i][1] <= 100
#######3
# >>> lst = [['a','b','c'], [1,2,3], ['x','y','z']]
# >>> lst2 = [item[0] for item in lst]
# >>> lst2
# ['a', 1, 'x']
# def stringShift(s, shift):
#     """
#     :type s: str
#     :type shift: List[List[int]]
#     :rtype: str
#     """
#     for i in shift:
#         saved = s
#         #print(i)
#         if i[0] == 0:
#             #for j in shift:
#                 #print(j)
#             if i[1]==1:
#                 s = s[1:]+s[0]
#             else:
#                 v = i[1]
#                 print(v)
#                 print(s[v:])
#                 s = s[v:]+s[:v]
#         elif i[0]==1:
#             if i[1]==1:
    
#                 s = s[-1]+s[:-1]
#             else:
#                 v = i[1]
#                 print(v)
#                 s = s[-v:]+s[:v+1]
#             if len(s) != saved:
#                 s = s[:len(saved)]  
#     print(s)
#     return s


# #to test the right shift
# def stringShifti(s,shift):
#     saved = s
#     for i in shift:
#         # print(i)
#         # print(i[0])
#         if i[0]==1:
#             #for j in shift:
#             print(i)
#             print(i[0])
#             if i[1]==1:

#                 s = s[-1]+s[:-1]
#             else:
#                 v = i[1]
#                 print(v)
#                 s = s[-v:]+s[:v+1]
#             if len(s) != saved:
#                 s = s[:len(saved)]
#             print(s)

def stringShift(s,shift):
    move_left = 0
    lenofstring = len(s)
    for direction, amount in shift:
        if direction ==0:
            move_left = move_left + amount
        else:
            move_left -= amount
    move_left = move_left%lenofstring
    return s[move_left:]+s[:move_left]

print(stringShift("hello",[[0,2],[1,2]]) )
#stringShifti("hello",[[0,1],[1,4]])