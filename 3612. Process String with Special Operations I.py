class Solution:
    def processStr(self, s: str) -> str:
        result = ""
        for letter in s:
            if letter == "#":
                result += result
            elif letter == "%":
                result = result[::-1]
            elif letter == "*":
                result = result[0:len(result) - 1]
            else:
                result += letter
        return result
