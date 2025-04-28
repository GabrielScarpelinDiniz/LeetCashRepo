# Problem Number 67 - Add Binary

> Given two binary strings a and b, return their sum as a binary string.

It's very easy to implement a solution converting the binary strings to integers, adding them, and then converting the result to binary string again.

But, improve my theoretical understanding of number addition, I made this using the conventional sum, adding each Binary

## How binary sum works?

Imagine that you have two number: 1011 and 1110. How does the sum between these two numbers work? To find the solution, lets remind how the decimal sum works

| Posição | Centenas | Dezenas | Unidades |
|---------|----------|---------|----------|
| Número 1 |     2    |    3    |     5    |
| Número 2 |     1    |    6    |     8    |
| Transporte |     1    |    1    |     0    |
| Resultado |     4    |    0    |     3    |

Basically, we start from the unit and sum: 5 + 8. The result is 13, but our numbers are decimal, this means that we cannot have numbers biggest than 9 in each column. So, what we do? Subtract 13 from 10 (our base) thats equal 3, and put the result. In sequence, we take the exactly division 13 by 10 (that is equal one). And then we put this number at next column to sum. And repeat those steps for each column.

In binary, is the same logic, but we only change our base from 10 to 2. And here is the code

```py
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        maxLen = max(len(a), len(b))
        if len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a
        elif len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b

        needToAdd = 0
        binaryStr = ""
        for idx in range(maxLen - 1, -1, -1):
            firstBinary = int(a[idx])
            secondBinary = int(b[idx])
            sum = firstBinary + secondBinary + needToAdd
            print(sum)
            if sum > 1:
                binNum = sum - 2
                binaryStr = str(binNum) + binaryStr
                needToAdd = sum // 2
            else:
                needToAdd = 0
                binaryStr = str(sum) + binaryStr

        if needToAdd == 1:
            binaryStr = "1" + binaryStr
        if needToAdd == 2:
            binaryStr = "10" + binaryStr
        return binaryStr
```

Commonly with our decimal numbers, the sum starts from the right. But, how we can have numbers with differents length, we start adding left zeros (that not change the number) and then, we follow those steps explained above.

1. Convert the two numbers to integer
2. Sum the two numbers and with the "transport" layer
3. If the sum is biggest than 1 (like is biggest than 9)
3. -> subtract two (like we subtracted 10 in the decimal example)
3. -> Put this number on the final number
3. -> Take the exactly division by two (explained above too)
4. If not:
4. -> We need to reset the transport layer and add the number on the final number

The steps 3 and 4 occurs in a loop, starting from right and going to left on the numbers.

And then, the final step is check if the last number check (the left number from the number), need an additional carry-over". If the transport layer is equal one, thats mean that we only have to put a number one at left. If the transport layer is equal two, thats mean that we need to put 10 at left of the Number
