func countStudents(students []int, sandwiches []int) int {
	attempts_per_sandwich := 0
	for len(students) > 0 && attempts_per_sandwich < len(students) {
		first_student := students[0]
		first_sandwich := sandwiches[0]

		if first_student == first_sandwich {
			attempts_per_sandwich = 0
			students = students[1:]
			sandwiches = sandwiches[1:]
		} else {
			attempts_per_sandwich = attempts_per_sandwich + 1
			students = students[1:]
			students = append(students, first_student)
		}
		fmt.Println(students)
	}
	return len(students)
}