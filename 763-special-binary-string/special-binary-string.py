class Solution:

    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        i = 0
        res = []

        for j, char in enumerate(s):
            count += 1 if char == "1" else -1
            if count == 0:
                # Recursively process the inner substring, rewrap with '1' and '0'
                inner_processed = self.makeLargestSpecial(s[i + 1 : j])
                res.append("1" + inner_processed + "0")
                i = j + 1

        # Sort sub-components in descending order to get the lexicographically largest result
        res.sort(reverse=True)
        return "".join(res)
