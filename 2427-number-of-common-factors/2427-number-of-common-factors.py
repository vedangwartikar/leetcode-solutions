class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        common = 0
        for i in range(1, max(a//2, b//2) + 1):
            if not a%i and not b%i:
                common += 1
        return common if a != b else common + 1