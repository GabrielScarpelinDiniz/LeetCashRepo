class Solution:
    def defangIPaddr(self, address: str) -> str:
        answer = []
        for i in address:
            if i == ".":
                answer.append("[")
                answer.append(".")
                answer.append("]")
            else:
                answer.append(i)

        print(answer)
        str_answer = ""
        for i in answer:
            str_answer += i
        return str_answer