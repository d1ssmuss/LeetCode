class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        # count = 0
        # i = 0
        # while i <= len(sandwiches):
        #     if sandwiches[i] in students:
        #         if students[0] == sandwiches[i]:
        #             count += 1
        #             i += 1
        #             students = students[1:]
        #         else:
        #             students = students[1:] + [students[0]]
        #     else:
        #         break
        # return count, len(students) - count

        count = 0
        len_students = len(students)
        while sandwiches[0] in students:
            if students[0] == sandwiches[0]:
                count += 1
                if len(sandwiches) > 1:
                    sandwiches = sandwiches[1:]
                    students = students[1:]
                else:
                    break
            else:
                students = students[1:] + [students[0]]
        return count, len_students - count



print(Solution().countStudents(students = [1,1,0,0], sandwiches = [0,1,0,1]))
print(Solution().countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]))
# print(Solution().countStudents())
