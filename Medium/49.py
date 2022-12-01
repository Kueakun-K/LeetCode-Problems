from typing import List
from collections import defaultdict
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    ans = defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return ans.values()

strs = ["eat","tea","tan","ate","nat","bat"]
# strs = ["ac","c"]
print(groupAnagrams(strs))