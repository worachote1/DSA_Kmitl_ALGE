class Solution:
    def reverseBits(self, n: int) -> int:
        data = []
        for i in range(32):
            data.append(n & 1)
            n = n>>1

        res = 0
        for i in range(len(data)):
            res = (res << 1) | data[i]

        return res