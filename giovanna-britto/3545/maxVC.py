class Solution:
    def maxFreqSum(self, s: str) -> int:
        vogais = 'aeiou'
        d = defaultdict(int)

        for ch in s: 
            d[ch] += 1

        maxVogal = max((d[ch] for ch in vogais), default = 0);
        for ch in vogais: 
            d[ch] = 0

        maxConso = max(d.values())
        return maxVogal + maxConso