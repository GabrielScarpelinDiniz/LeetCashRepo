class Solution:
    def defangIPaddr(self, address: str) -> str:
        addr = ""
        for i in address:
            if i == ".":
                addr += "[.]"
            else:
                addr += i
        
        return addr