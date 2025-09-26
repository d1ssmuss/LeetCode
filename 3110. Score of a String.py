def scoreOfString(s):
    """
    :type s: str
    :rtype: int
    """
    sum = 0
    for letter in range(0, len(s) - 1):
        if ord(s[letter]) < ord(s[letter + 1]):
            sum += -1 * (ord(s[letter]) - ord(s[letter + 1]))
        else:
            sum += ord(s[letter]) - ord(s[letter + 1])
    return sum

print(scoreOfString(input()))