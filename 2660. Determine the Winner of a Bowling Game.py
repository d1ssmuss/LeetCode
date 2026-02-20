class Solution(object):
    def isWinner(self, player1, player2):
        """
        :type player1: List[int]
        :type player2: List[int]
        :rtype: int
        """
        score_1 = 0
        score_2 = 0
        for i in range(len(player1)):
            current = player1[i]
            if i == 0:
                score_1 += current
            else:
                prev = player1[i - 1]
                prev_prev = player1[i - 2]
                if (prev == 10 and i - 1 >= 0) or (prev_prev == 10 and i - 2 >= 0):
                    score_1 += current * 2
                else:
                    score_1 += current
            # print(player1, score_1, "!")
        for i in range(len(player2)):
            current = player2[i]
            if i == 0:
                score_2 += current
            else:
                prev = player2[i - 1]
                prev_prev = player2[i - 2]
                if (prev == 10 and i - 1 >= 0) or (prev_prev == 10 and i - 2 >= 0):
                    score_2 += current * 2
                else:
                    score_2 += current
        # print('Счёт', score_1, score_2)
        if score_1 > score_2:
            return 1
        elif score_2 > score_1:
            return 2
        else:
            return 0



print(Solution().isWinner(player1 = [5,10,3,2], player2 = [6,5,7,3]), 1)
print(Solution().isWinner(player1 = [3,5,7,6], player2 = [8,10,10,2]), 2)
print(Solution().isWinner(player1 = [2,3], player2 = [4,1]), 0)
print(Solution().isWinner(player1 = [1,1,1,10,10,10,10], player2 = [10,10,10,10,1,1,1]), 2)
print(Solution().isWinner([5,6,1,10], [5,1,10,5]), 2)