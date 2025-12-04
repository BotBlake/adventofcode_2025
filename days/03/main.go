package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func largest_subsequence_number(digits []int, k int) []int {
	stack := []int{}
	to_remove := len(digits) - k

	for _, d := range digits {
		for len(stack) > 0 && to_remove > 0 && stack[len(stack)-1] < d {
			stack = stack[:len(stack)-1] // pop
			to_remove--
		}
		stack = append(stack, d)
	}

	if len(stack) > k {
		return stack[:k]
	}
	return stack
}

func max_joltage_k_digits(bank_str string, k int) int {
	digits := []int{}
	for _, ch := range strings.TrimSpace(bank_str) {
		d, err := strconv.Atoi(string(ch))
		if err != nil {
			panic(err)
		}
		digits = append(digits, d)
	}

	chosen := largest_subsequence_number(digits, k)

	// Convert chosen digits back to integer
	resultStr := ""
	for _, d := range chosen {
		resultStr += strconv.Itoa(d)
	}

	result, err := strconv.Atoi(resultStr)
	if err != nil {
		panic(err)
	}
	return result
}

func main() {
	total_2 := 0
	total_12 := 0

	file, err := os.Open("days/03/puzzle_input.txt")
	if err != nil {
		panic(err)
	}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		line = strings.TrimSpace(line)
		if line == "" {
			continue
		}

		best2 := max_joltage_k_digits(line, 2)
		best12 := max_joltage_k_digits(line, 12)

		total_2 += best2
		total_12 += best12
	}

	fmt.Println("---------- SOLUTION DAY 03 ----------")
	fmt.Printf("Part 1: (2 digits):   %d\n", total_2)
	fmt.Printf("Part 2: (12 digits):  %d\n", total_12)
	fmt.Println("-----------------------------------")
}
