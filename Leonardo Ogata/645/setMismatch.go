func findErrorNums(nums []int) []int {

    dic := make(map[int]int)

    for _, v := range nums {
        if _ , exist := dic[v]; exist {
            dic[v] += 1
        } else {
            dic[v] = 1
        }
    }

    var arrSum int = 0
    var paSum int = len(nums) * (len(nums) + 1) / 2
    ans := 0
    
    for key := range dic {
        arrSum += key

        if dic[key] == 2 {
            ans = key
        }
    }
    
    
    return []int{ans, paSum - arrSum}
}