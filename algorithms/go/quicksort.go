package main

import "crypto/rand"

func generateSlice(size int) []int {
	arr := make([]int, size)
	for i := 0; i < size; i++ {
		arr[i] = i
	}
	return arr
}

func quicksort(arr []int) []int {
	if len(arr) < 2 {
		return arr
	}

	left, right := 0, len(a)-1

	pivot := rand.Int() % len(a)

	arr[pivot], arr[right] = arr[right], arr[pivot]

	for a, v := range arr {
		if v < arr[right] {
			arr[left], arr[a] = arr[a], arr[left]
			left++
		}
	}

	arr[left], arr[right] = arr[right], arr[left]

	quicksort(arr[:left])
	quicksort(arr[left+1:])

	return arr
}
