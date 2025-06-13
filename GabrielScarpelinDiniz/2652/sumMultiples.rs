impl Solution {
    pub fn sum_of_multiples(n: i32) -> i32 {
        let mut num = 1;
        let mut sum = 0;
        while num <= n {
            if num % 3 == 0 || num % 5 == 0 || num % 7 == 0 {
                sum = sum + num;
            }
            num += 1;
        }
        sum
    }
}
