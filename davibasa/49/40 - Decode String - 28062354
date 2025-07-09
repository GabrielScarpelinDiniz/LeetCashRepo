public class Solution {
    public string DecodeString(string s) {
        Stack<int> counts = new Stack<int>();
        Stack<StringBuilder> resultStack = new Stack<StringBuilder>();
        StringBuilder current = new StringBuilder();
        int k = 0;

        foreach (char ch in s) {
            if (char.IsDigit(ch)) {
                k = k * 10 + (ch - '0');
            } else if (ch == '[') {
                counts.Push(k);
                resultStack.Push(current);
                current = new StringBuilder();
                k = 0;
            } else if (ch == ']') {
                StringBuilder decodedString = resultStack.Pop();
                int currentK = counts.Pop();
                for (int i = 0; i < currentK; i++) {
                    decodedString.Append(current);
                }
                current = decodedString;
            } else {
                current.Append(ch);
            }
        }

        return current.ToString();
    }
}
