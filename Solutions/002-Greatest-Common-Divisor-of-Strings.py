class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # Check if both strings can be built from the same pattern
        if str1 + str2 != str2 + str1:
            return ""

        # Find GCD of lengths
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        length = gcd(len(str1), len(str2))

        return str1[:length]
