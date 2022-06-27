package main

func binarysearch(arr []int, value int) int {
	low := 0
	high := len(arr) - 1
	for low <= high {
		mid := (low + high) / 2
		if arr[mid] == value {
			return mid
		}
		if arr[mid] < value {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	return -1
}
