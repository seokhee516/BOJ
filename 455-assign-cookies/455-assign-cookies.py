class Solution(object):
    def findContentChildren(self, g, s):
        ans = 0
        s.sort(reverse=True)
        g.sort(reverse=True)

        while g and s:
            while s and s[-1] < g[-1]:
                s.pop()
            if s:
                if s[-1]>=g[-1]:
                    ans += 1
                s.pop()
                g.pop()
        return ans