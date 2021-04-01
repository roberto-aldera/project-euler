// Problem 003
// The prime factors of 13195 are 5, 7, 13 and 29.
// What is the largest prime factor of the number 600851475143?

package main

import "fmt"

func get_largest_prime_factor(n int) int {
	p := 2
	for p*p < n {
		if n%p == 0 {
			n = n / p
		} else {
			// p won't always be prime, but it'll give a non-zero remainder in that case,
			// and be incremented until it divides in to n
			p += 1
		}
	}
	return n
}

func main() {
	fmt.Println("Answer to problem 003:", get_largest_prime_factor(600851475143))
}
