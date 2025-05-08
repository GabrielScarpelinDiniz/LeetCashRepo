# Problem 199

> Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# How the problem works?

I spend a lot of time trying to understanding the problem. Because I have some difficult to understand what the problem means with "Yourself on the right side". But is this. We need to imagine yourself literally on the right of the tree, and when we look to the tree which nodes we will see?

# How I solve the problem?

This is a classic problem that we can use DFS, a search that uses the depth. I select in my dfs to start always from the right, so the algorithm will go maximium to the right first. After this, the algorithm will look to the others elements, and will add this element to the output, if this elements have more depth than the element most to the right. I made this sharing a variable with the functions, this variable cannot be a number only because we need to pass the memory reference for the other function, because this, I decide to use the Dict.
