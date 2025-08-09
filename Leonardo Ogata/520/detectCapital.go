func detectCapitalUse(word string) bool {
    if len(word) == 1 {
        return true
    }

    firstLetter := []rune(word)[0]
    secondLetter := []rune(word)[1]

    if unicode.IsUpper(firstLetter){
        if unicode.IsUpper(secondLetter){
            for _, r := range word {
                if !unicode.IsUpper(r) {
                    return false
                }
            } 
        } else {
            i := 0
            for _, r := range word {
                if unicode.IsUpper(r) && i > 0 {
                    return false
                }
                i++
            } 
        }
        
    } else {
        for _, r := range word {
            if unicode.IsUpper(r) {
                    return false
                }
        }
    }

    return true
    
}