class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        return [[pixel ^ 1 for pixel in row[::-1]] for row in image]