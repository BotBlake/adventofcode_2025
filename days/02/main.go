package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type RangeAnalyzer struct {
	simple_invalid_id_sum      int
	complicated_invalid_id_sum int
}

func NewRangeAnalyzer() *RangeAnalyzer {
	return &RangeAnalyzer{}
}

// Check if ID is made of 2 repeated halves (e.g., 1212 → "12" + "12")
func (r *RangeAnalyzer) is_simply_invalid(id int) bool {
	id_str := strconv.Itoa(id)
	length := len(id_str)

	if length%2 != 0 {
		return false
	}

	half := length / 2
	return id_str[:half] == id_str[half:]
}

// Check if ID is made of *any* repeating block (e.g., 123123123)
func (r *RangeAnalyzer) is_complicated_invalid(id int) bool {
	id_str := strconv.Itoa(id)
	n := len(id_str)

	for size := 1; size <= n/2; size++ {
		if n%size == 0 {
			block := id_str[:size]
			if strings.Repeat(block, n/size) == id_str {
				return true
			}
		}
	}
	return false
}

func (r *RangeAnalyzer) analyze_range(start, end int) {
	for id := start; id <= end; id++ {
		if r.is_simply_invalid(id) {
			r.simple_invalid_id_sum += id
		}
		if r.is_complicated_invalid(id) {
			r.complicated_invalid_id_sum += id
		}
	}
}

func (r *RangeAnalyzer) get_simple_invalid_id_count() int {
	return r.simple_invalid_id_sum
}

func (r *RangeAnalyzer) get_complicated_invalid_id_sum() int {
	return r.complicated_invalid_id_sum
}

func main() {
	data, err := os.ReadFile("days/02/puzzle_input.txt")
	if err != nil {
		panic(err)
	}

	analyzer := NewRangeAnalyzer()

	ranges := strings.SplitSeq(strings.TrimSpace(string(data)), ",")
	for rng := range ranges {
		parts := strings.Split(rng, "-")

		start, err1 := strconv.Atoi(parts[0])
		end, err2 := strconv.Atoi(parts[1])

		if err1 != nil || err2 != nil {
			panic("Invalid range in input file")
		}

		analyzer.analyze_range(start, end)
	}

	fmt.Println("----------SOLUTION DAY 02----------")
	fmt.Printf("Part1: Easy invalid ID sum %d.\n", analyzer.get_simple_invalid_id_count())
	fmt.Printf("Part2: All invalid ID sum %d.\n", analyzer.get_complicated_invalid_id_sum())
	fmt.Println("-----------------------------------")
}
