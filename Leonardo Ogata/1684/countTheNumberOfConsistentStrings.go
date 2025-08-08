func countConsistentStrings(allowed string, words []string) int {

    counter := len(words)

    dic := make(map[rune]struct{})
    
    for _, r := range allowed {
        dic[r] = struct{}{}
    }

    for _, word := range words {
        for _, char := range word {
            if _, exists := dic[char]; !exists{
                counter--
                break
            }
        }
    }

    return counter
}