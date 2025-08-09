class Solution {
    public String reverseWords(String s) {
        StringBuilder res = new StringBuilder();
        int fast = s.length() - 1;
        int slow = fast;

        while(fast >= 0){
            if(s.charAt(fast) == ' ' && s.charAt(slow) == ' '){
                fast --;
                slow --;
            } else if(s.charAt(fast) != ' '){
                fast --;
            } else {
                for(int i = fast + 1; i <= slow; i++){
                    res.append(s.charAt(i));
                }

                res.append(' ');
                slow = fast;
            }
        }

        System.out.println(slow);
        System.out.println(fast);
        
        if(slow == fast){
            res.deleteCharAt(res.length() - 1);
        } else {
            for(int i = fast + 1; i <= slow; i++){
                res.append(s.charAt(i));
            }
        }

        return res.toString();
    }
}