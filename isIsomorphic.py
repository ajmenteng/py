class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        dc1 = {}
        dc2 = {}
        if len(s) != len(t):
            print("False")
        else:
            for i in range(len(s)):
                if dc1.get(s[i]) is None and dc2.get(t[i]) is None:
                    dc1[s[i]] = t[i]
                    dc2[t[i]] = s[i]
                elif dc1.get(s[i]) != t[i] or dc2.get(t[i]) != s[i]:
                    return False
                    break
            else:
                return True