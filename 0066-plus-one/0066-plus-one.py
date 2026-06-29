class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        r = 0 

        for i in digits:
            r = r * 10 + i

        result =  r + 1 

        out = [int(d) for d in str(result)]

        return out

