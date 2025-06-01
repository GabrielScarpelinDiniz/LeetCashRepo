class Solution {

    public int countMatches(
        List<List<String>> items,
        String ruleKey,
        String ruleValue
    ) {
        int count = 0;
        for (var item : items) {
            if (ruleKey.equals("type") && ruleValue.equals(item.get(0))) {
                count++;
            } else if (
                ruleKey.equals("color") && ruleValue.equals(item.get(1))
            ) {
                count++;
            } else if (
                ruleKey.equals("name") && ruleValue.equals(item.get(2))
            ) {
                count++;
            }
        }
        return count;
    }
}
