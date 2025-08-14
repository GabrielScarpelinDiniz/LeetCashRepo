func reverseDegree(s string) int {
	letras := make(map[rune]int)

	for i := 0; i < 26; i++ {
		letra := rune('a' + i)
		letras[letra] = 26 - i
	}

    sum := 0

    for i, char := range s {
        sum += letras[char] * (i+1)
    }
    
    return sum
    
}