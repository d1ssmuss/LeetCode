class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        # days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        months = {
            0: 0,
            1: 31,
            2: 59,
            3: 90,
            4: 120,
            5: 151,
            6: 181,
            7: 212,
            8: 243,
            9: 273,
            10: 304,
            11: 334,
            12: 365,
        }
        arriveAlice_month, arriveAlice_day = arriveAlice.split('-')
        leaveAlice_month, leaveAlice_day = leaveAlice.split('-')
        arriveBob_month, arriveBob_day = arriveBob.split('-')
        leaveBob_month, leaveBob_day = leaveBob.split('-')
        Alice_days_arrive = months[(int(arriveAlice_month) - 1)] + int(arriveAlice_day)
        Alice_days_leave = months[(int(leaveAlice_month) - 1)] + int(leaveAlice_day)
        Bob_days_arrive = months[(int(arriveBob_month) - 1)] + int(arriveBob_day)
        Bob_days_leave = months[(int(leaveBob_month) - 1)] + int(leaveBob_day)
        print(Alice_days_arrive, Alice_days_leave, Bob_days_arrive, Bob_days_leave)
        if max(Alice_days_arrive, Bob_days_arrive) <= min(Alice_days_leave, Bob_days_leave):
            return abs(max(Alice_days_arrive, Bob_days_arrive) - min(Alice_days_leave, Bob_days_leave)) + 1
        else:
            return 0
