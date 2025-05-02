import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        
        for(char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            }

            if (c == ')' && stack.isEmpty()|| c == '}' && stack.isEmpty() || c == ']' && stack.isEmpty()) {
                return false;
            }

            if (c == ')') {
                char check = stack.peek(); 
                    if (check == '(') {
                        stack.pop();
                    }else{
                        return false;
                    }
            }

            if (c == '}') {
                char check = stack.peek(); 
                    if (check == '{') {
                        stack.pop();
                    }else{
                        return false;
                    }
            }

            if (c == ']') {
                char check = stack.peek(); 
                    if (check == '[') {
                        stack.pop();
                    }else{
                        return false;
                    }
            }
        }

        if (stack.isEmpty()) {
            return true;
        }else{
            return false;
        }
        
    
    }
}