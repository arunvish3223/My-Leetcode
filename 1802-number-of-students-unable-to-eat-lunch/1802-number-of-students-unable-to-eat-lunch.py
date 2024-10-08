class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        dict1 = {}

        for i in students:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1

        for s in sandwiches:
            if dict1.get(s, 0) > 0:
                res -= 1
                dict1[s] -= 1
            else:
                break

        return res
