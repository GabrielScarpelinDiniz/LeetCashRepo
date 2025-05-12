class Solution {
    public boolean isValid(String s) {
        if(s.length() <= 1) return false;
        Stack<Character> parentheses = new Stack<>();

        for(int i = 0; i < s.length(); i++){
            switch(s.charAt(i)){
                case '(':
                    parentheses.push('(');
                    break;
                case ')':
                    if(!parentheses.isEmpty() && parentheses.peek() == '(')parentheses.pop();
                    else return false;
                    break;
                case '[':
                    parentheses.push('[');
                    break;
                case ']':
                    if(!parentheses.isEmpty() && parentheses.peek() == '[') parentheses.pop();
                    else return false;
                    break;
                case '{':
                    parentheses.push('{');
                    break;
                case '}':
                    if(!parentheses.isEmpty() && parentheses.peek() == '{') parentheses.pop();
                    else return false;
                    break;
            }
        }
        if(parentheses.isEmpty()) return true;
        return false;
    }
}