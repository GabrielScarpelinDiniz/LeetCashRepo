func findRelativeRanks(score []int) []string {
    dic := make(map[int]string)

    for _, v := range score{
        dic[v] = ""
    }

    keys := make([]int, 0, len(dic))
    for k := range dic {
        keys = append(keys, k)
    }
    
    sort.Sort(sort.Reverse(sort.IntSlice(keys)))

    for i, key := range keys{
        if i == 0 {
            dic[key] = "Gold Medal"
        } else if i == 1{
            dic[key] = "Silver Medal"
        } else if i == 2 {
            dic[key] = "Bronze Medal"
        } else {
            dic[key] = strconv.Itoa(i + 1)
        }
    }

    fmt.Print(dic)

    ans := make([]string, len(score))

    for i, value := range score {
        ans[i] = dic[value]
    }

    fmt.Print(ans)

    return ans
}