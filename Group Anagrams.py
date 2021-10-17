class Solution(object):
    def groupAnagrams(self, strs):
        
        ans = collections.defaultdict(list)
        print(ans)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
       
        return ans.values()
        
