class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""

        n1 = len(word1)
        n2 = len(word2)

        for i in range(min(n1, n2)):
            result += word1[i] + word2[i]

        result += word1[min(n1, n2):]
        result += word2[min(n1, n2):]

        return result
