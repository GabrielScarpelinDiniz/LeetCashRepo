class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        movimentos = 0

        for i in range(len(seats)):
            movimentos += abs(seats[i] - students[i])
        
        return movimentos