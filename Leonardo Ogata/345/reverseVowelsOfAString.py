class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = []
        arrV = []

        for x in s:
            if (x == 'a' or x == 'e' or x == 'i' or 
        x == 'o' or x == 'u' or x == 'A' or 
        x == 'E' or x == 'I' or x == 'O' or 
        x == 'U'):
                arrV.append(x)
            arr.append(x)

        for i in range(len(arr)):
            if (arr[i] == 'a' or arr[i] == 'e' or arr[i] == 'i' or 
        arr[i] == 'o' or arr[i] == 'u' or arr[i] == 'A' or 
        arr[i] == 'E' or arr[i] == 'I' or arr[i] == 'O' or 
        arr[i] == 'U'):
                arr[i] = arrV[-1]
                arrV.pop()
        
        string = "".join(arr)

        return string
        
        


        
        