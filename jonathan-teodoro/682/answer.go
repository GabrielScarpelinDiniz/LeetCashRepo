func calPoints(operations []string) int {
	stack := []string{}
	for _, value := range operations {
		if value == "+" {
			if len(stack) < 2 {
				stack = append(stack, stack[len(stack)-1])
				continue
			}
			val1, _ := strconv.Atoi(stack[len(stack)-1])
			val2, _ := strconv.Atoi(stack[len(stack)-2])
			stack = append(stack, strconv.Itoa(val1+val2))
		} else if value == "C" {
			stack = stack[:len(stack)-1]
		} else if value == "D" {
			val, _ := strconv.Atoi(stack[len(stack)-1])
			stack = append(stack, strconv.Itoa(val*2))
		} else {
			stack = append(stack, value)
		}
		fmt.Println(stack)
	}
	if len(stack) > 0 {
		sum := 0
		for _, value := range stack {
			int_value, _ := strconv.Atoi(value)
			sum = sum + int_value
		}
		return sum
	}
	return 0

}