class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Function to convert a negative number to its two's complement representation
        def two_complement(x):
            if x < 0:
                x = (1 << 32) + x
            return x

        a = two_complement(a)
        b = two_complement(b)
        

        mask = 0xFFFFFFFF

        while b != 0:
            # Calculate carry bits
            carry = (a & b) << 1
            # Sum bits without considering carry
            a = (a ^ b) & mask
            # Carry becomes the new b
            b = carry & mask

        # If the result is a negative number in two's complement form, convert it back
        if a > 0x7FFFFFFF:
            a = ~(a ^ mask)

        return a
