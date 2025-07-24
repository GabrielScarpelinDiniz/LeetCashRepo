package main

func pivotIndex(nums []int) int {
	totalSum := 0
	leftSum := 0

	for _, num := range nums {
		totalSum += num
	}

	for i, num := range nums {
		totalSum -= num

		if leftSum == totalSum {
			return i
		}

		leftSum += num
	}

	return -1
}
