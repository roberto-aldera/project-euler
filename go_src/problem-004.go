// Problem 004
// A palindromic number reads the same both ways. The largest palindrome made
// from the product of two 2-digit numbers is 9009 = 91 × 99. Find the largest
// palindrome made from the product of two 3-digit numbers.

package main

import (
	"fmt"
	"strings"
)

func getReverse(orig string) string {
	c := strings.Split(orig, "")
	end_index := len(c) - 1
	for i := 0; i < end_index-i; i++ {
		c[i], c[end_index-i] = c[end_index-i], c[i]
	}
	return strings.Join(c, "")
}

func checkIfPalindrome(candidate int) bool {
	forward_reading := fmt.Sprint(candidate)
	return forward_reading == getReverse(forward_reading)
}

// Palindrome should be in the form abccba
// So expand to 100000a + 10000b + 1000c + 100c + 10b + 1a
// Becomes 100001a + 10010b + 1100c, which is divisible by 11, so palindrome
// must be too 11 is prime, so one of the two 3-digit factors must be too, so we
// need only check those cases
func getLargestPalindrome() int {
	p1 := 999
	p2 := 990
	var largest_palindrome int

	for p1 > 100 {
		p2 = 990
		for p2 > 100 {
			candidate := p1 * p2
			if checkIfPalindrome(candidate) {
				if candidate > largest_palindrome {
					largest_palindrome = candidate
				}
			}
			p2 -= 11
		}
		p1--
	}
	return largest_palindrome
}

func main() {
	fmt.Println("Answer to problem 004:", getLargestPalindrome())
}
