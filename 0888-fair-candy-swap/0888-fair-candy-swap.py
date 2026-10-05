class Solution:

    def fairCandySwap(
        self, aliceSizes: list[int], bobSizes: list[int]
    ) -> list[int]:
        sum_a = sum(aliceSizes)
        sum_b = sum(bobSizes)
        diff = (sum_b - sum_a) // 2

        bob_set = set(bobSizes)

        for x in aliceSizes:
            target = x + diff
            if target in bob_set:
                return [x, target]