def maximumWealth(accounts):
    """
    :type accounts: List[List[int]]
    :rtype: int
    """
    return max([sum(accounts[i]) for i in range(len(accounts))])


a = maximumWealth([[1,2,3],[3,2,1]])
print(a)