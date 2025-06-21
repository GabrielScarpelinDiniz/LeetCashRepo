class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        resposta = []
        for i in range(len(accounts)):
            somas = 0
            for j in accounts[i]:
                somas += j
            resposta.append(somas)
        return max(resposta)
