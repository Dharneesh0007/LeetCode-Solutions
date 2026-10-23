import math
from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        return math.gcd(*Counter(deck).values()) > 1