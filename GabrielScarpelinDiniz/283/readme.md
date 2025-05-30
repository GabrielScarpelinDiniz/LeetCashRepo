# Problem 283

> Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

> Note that you must do this in-place without making a copy of the array.

# How does I solve the Problem?

First, I iterate in each number, saving one thing: the index of the last zero that I've put at the final. So then, I iterate across the array, if the current number is equal 0, we move he to the final (or the position before the last zero that I put). If I not put zeros at the final, when we find a zero, go with him to the final, always.
