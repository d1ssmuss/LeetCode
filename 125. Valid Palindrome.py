class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = [i for i in s if i.isdigit() or i.isalpha()]
        return True if ''.join(a).lower() == ''.join(a).lower()[::-1] else False
        # return True if ''.join([i for i in s if i.isalpha()]).lower() == ''.join([i for i in s if i.isalpha()]).lower()[::-1] else False


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome(" "))
print(Solution().isPalindrome("0P"))
print(Solution().isPalindrome("1b1"))

