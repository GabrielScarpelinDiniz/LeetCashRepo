# Problem 136

> Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

> You must implement a solution with a linear runtime complexity and use only constant extra space.

# How does I solve the problem?

Found a solution in O(n²) it's so easy, so I try to implement a solution that takes only O(n) complexity. To solve in a complexity time O(n), I create two set (set is a data structure that dont accept repeated element, and we can find if the element was on set closely to O(1) complexity time). The first set is for elements who has appeared before in the array, the second set is for element that appears only one time in the array (called potential_items), if the element has appeared before, we remove the element from the set that saves the potential_items, otherwise we add the element in the appeared elements set, and in the potential elements set. At the final, we will have only a unic element in the potential items set, because the question said that we have only one element that appears one times.
