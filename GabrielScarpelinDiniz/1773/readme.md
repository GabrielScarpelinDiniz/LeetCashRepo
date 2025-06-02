# Problem 1773

> You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

> The ith item is said to match the rule if one of the following is true:

`ruleKey == "type" and ruleValue == typei.`
`ruleKey == "color" and ruleValue == colori.`
`ruleKey == "name" and ruleValue == namei.`
`Return the number of items that match the given rule.`

# How does I solve the problem?

First, I iterate for each item in the array, if an item match if the rule above (in the problem requirements) I adds one in a variable called count. I use else if, because if need to match exactly with one rule, otherwise, we dont need to add in the count.
