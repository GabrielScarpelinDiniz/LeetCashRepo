class Solution:
    def interpret(self, command: str) -> str:
        newCommand = command.replace('()', 'o').replace('(al)', 'al')

        return newCommand