package main

func euclids(a, b int) int {
	if b == 0 {
		return a
	}
	return euclids(b, a%b)
}
