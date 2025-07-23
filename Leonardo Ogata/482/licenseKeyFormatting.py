class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        if s == "-":
            return ""
        elif len(s) == 1:
            return s.upper()

        ans = ""
        dashes = 0
        for i in s:
            if i == "-":
                dashes += 1 

        rest = (len(s) - dashes) % k

        s = s.replace("-", "")

        counter = 0

        if rest != 0:
            for i in range(rest):
                ans += s[counter]
                counter += 1
            ans += "-"

        i = 1
        while counter < len(s):
            print(counter, len(s))
            if i % k == 0 and i != 0 and counter != len(s) -1:
                ans += s[counter]
                ans += "-"
            else: 
                ans += s[counter]
            counter += 1
            i += 1
        
        return ans.upper()