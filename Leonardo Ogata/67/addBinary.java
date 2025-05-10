import java.math.BigInteger;

class Solution {
    public String addBinary(String a, String b) {

        // long decA = 0;
        // long decB= 0;

        // int p = 0;
        // for (int i =  a.length() - 1; i >= 0; i--) {
        //     decA += Character.getNumericValue(a.charAt(i)) * Math.pow(2, p);
        //     p ++;
        // }

        // p = 0;
        // for (int i =  b.length() - 1; i >= 0; i--)  {
        //     decB += Character.getNumericValue(b.charAt(i)) * Math.pow(2, p); 
        //     p++;
        // }

        // long temp = decA + decB;

        // StringBuilder result = new StringBuilder();
        // if (temp == 0) {
        //     result.append("0");
        // } else {
        //     while (temp > 0) {
        //         result.append(temp % 2);
        //         temp = temp / 2;
        //     }
        //     result.reverse();
        // }

        // return result.toString();
        
        BigInteger numA = new BigInteger(a, 2); 
        BigInteger numB = new BigInteger(b, 2);
        BigInteger sum = numA.add(numB);         
        return sum.toString(2); 
              

    }
}