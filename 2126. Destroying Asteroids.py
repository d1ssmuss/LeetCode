class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        # maximus = [i for i in asteroids if i <= mass]
        # while maximus != []:
        #     mx = max(maximus)
        #     mass += mx
        #     asteroids.remove(mx)
        #     maximus = [i for i in asteroids if i <= mass]
        #     # print(maximus)
        # return asteroids == []
        asteroids.sort()
        for i in asteroids:
            if mass >= i:
                mass += i
            else:
                return False
        return True


print(Solution().asteroidsDestroyed(mass = 10, asteroids = [3,9,19,5,21]))
print(Solution().asteroidsDestroyed(mass = 5, asteroids = [4, 9, 23, 4]))

