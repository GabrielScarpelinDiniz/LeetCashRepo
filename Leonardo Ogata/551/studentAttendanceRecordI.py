class Solution:
    def checkRecord(self, s: str) -> bool:
        late = 0
        absent = 0

        for i in s:
            if i == 'L':
                late += 1
            if i == 'A':
                late = 0
                absent += 1
            if i == 'P':
                late = 0
            if late == 3 or absent == 2:
                return False
        
        return True
            
        