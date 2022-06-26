package main

func countingsort(arr []int) []int {
	if len(arr) < 2 {
		return arr
	}
	pivot := arr[0]
	left, right := []int{}, []int{}
	for _, v := range arr[1:] {
		if v < pivot {
			left = append(left, v)
		} else {
			right = append(right, v)
		}
	}
	return append(append(countingsort(left), pivot), countingsort(right)...)
}
