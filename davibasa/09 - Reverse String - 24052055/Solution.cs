public class Solution {
   public void ReverseString(char[] s) {
        int esq = 0;
        int dir = s.Length - 1;
        
        while (esq < dir) {
            char temp = s[esq];
            s[esq] = s[dir];
            s[dir] = temp;
            
            esq++;
            dir--;
        }
    }
}