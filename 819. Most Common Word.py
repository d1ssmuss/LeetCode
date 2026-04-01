class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        for i in "!?',;.":
            paragraph = paragraph.replace(i, ' ')
        paragraph = paragraph.lower()
        d = {}
        for word in paragraph.split():
            if word in d:
                d[word] += 1
            elif word not in banned:
                d[word] = 1
        print(sorted(d.items(), key=lambda item: item[1]))
        return sorted(d.items(), key=lambda item: item[1])[-1][0]

print(Solution().mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))
print(Solution().mostCommonWord(paragraph = "a.", banned = []))
print(Solution().mostCommonWord(paragraph = "Bob. hIt, baLl", banned = ["bob", "hit"]))
print(Solution().mostCommonWord(paragraph = "a b.b", banned = []))
