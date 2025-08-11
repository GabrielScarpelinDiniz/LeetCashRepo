func kidsWithCandies(candies []int, extraCandies int) []bool {

    arr := make([]bool, len(candies))

    biggest := 0

    for _, v := range candies {
        if v > biggest {
            biggest = v
        }
    }

    for i, v := range candies {
        if v + extraCandies >= biggest{
            arr[i] = true
        } else {
            arr[i] = false
        }
    }

    return arr
}