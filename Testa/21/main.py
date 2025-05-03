class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i_map = {}
        left = 0 
        length = 0

        for right, char in enumerate(s):
            if char in i_map and i_map[char] >= left:
                left = i_map[char] + 1
            
            i_map[char] = right
            length = max(length, right - left + 1) 

        return length

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))