# def groupAnagrams(strs):

#     """
#     :type strs: List[str]
#     :rtype: List[List[str]]
#     """
#     newstrarr = []
#     for i in range(1,len(strs)):
#         for j in range(len(strs[i])):
#             if strs[i][j:] and strs[i][0:j] in strs[i-1]==True:
#                 newstrarr.append(strs[i])

# GROUP ANAGRAMS
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
def groupAnagrams(strs):
    ans = collections.defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return ans.values()

#  def groupAnagrams(strs):
#         ans = collections.defaultdict(list)
#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c) - ord('a')] += 1
#             ans[tuple(count)].append(s)
#         return ans.values()

# groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
