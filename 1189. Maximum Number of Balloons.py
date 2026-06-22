class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        # 0 ms
        # d = {}
        # d['b'] = text.count('b')
        # d['a'] = text.count('a')
        # d['l_1'] = text.count('l') // 2
        # d['l_2'] = text.count('l') - d['l_1']
        # d['o_1'] = text.count('o') // 2
        # d['o_2'] = text.count('o') - d['o_1']
        # d['n'] = text.count('n')
        # return d, d.values(), min(d.values())

        d = {i : 0 for i in 'balon'}
        for i in text:
            if i in 'balon':
                d[i] += 1
        d['l'] = d['l'] // 2
        d['o'] = d['o'] // 2
        return min(d.values())



print(Solution().maxNumberOfBalloons("nlaebolko"))
print(Solution().maxNumberOfBalloons("loonbalxballpoon"))
print(Solution().maxNumberOfBalloons("leetcode"))
print(Solution().maxNumberOfBalloons("balon"))
print(Solution().maxNumberOfBalloons("krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"))
