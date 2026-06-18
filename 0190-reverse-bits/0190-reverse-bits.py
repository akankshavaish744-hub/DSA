class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_num = 0

        for i in range(32):
            last_bit = n % 2
            reversed_num = reversed_num * 2 + last_bit
            n //= 2

        return reversed_num