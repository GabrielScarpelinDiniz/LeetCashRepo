class Solution {
    public String addBinary(String a, String b) {
        int carried = 0;
        StringBuilder res = new StringBuilder();
        int pa = a.length() - 1;
        int pb = b.length() - 1;

        while(pa >= 0 || pb >= 0){
            int intA = pa >= 0? Character.getNumericValue(a.charAt(pa)): 0;            
            int intB = pb >= 0? Character.getNumericValue(b.charAt(pb)): 0;

            if(intA + intB + carried > 1){
                if (intA + intB + carried == 2) res.append('0');
                if (intA + intB + carried == 3) res.append('1');
                carried = 1;
            } else if (intA + intB + carried == 1) {
                res.append('1');
                carried = 0;
            } else {
                res.append('0');
                carried = 0;
            }
                pa --;
                pb --;
        
        }

        if(carried == 1) res.append('1');
        res.reverse();
        return res.toString();
    }
}