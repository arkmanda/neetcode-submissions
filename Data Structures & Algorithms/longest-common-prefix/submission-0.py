class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x = 201
        for strg in strs:
            if(len(strg) < x):
                x = len(strg)
        for i in range(x):
            a = strs[0][i]
            for j in range(1,len(strs)):
                if(strs[j][i]!=a):
                    return strs[0][0:i]
        return strs[0][0:x]   
        