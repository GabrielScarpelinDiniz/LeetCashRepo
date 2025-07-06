class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        func = 0
        for i in range(len(hours)):
            if hours[i] >= target:
                func+= 1

        return func