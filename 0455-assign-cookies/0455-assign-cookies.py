class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        i = 0
        n = len(g)
        
        if n == 0 or not s:
            return 0
            
        for cookie in s:
            if cookie >= g[i]:
                i += 1
                if i == n:
                    break
                    
        return i