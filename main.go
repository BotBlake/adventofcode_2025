package main

import (
	"fmt"
	"os"
	"os/exec"
	"strconv"
	"time"
)

func getTodayDay() (int, error) {
	today := time.Now()
	if today.Month() != time.December {
		return 0, fmt.Errorf("it is not December; please specify a day explicitly")
	}
	return today.Day(), nil
}

func runDay(day int) error {
	dayStr := fmt.Sprintf("%02d", day)
	path := fmt.Sprintf("days/%s/main.go", dayStr)

	cmd := exec.Command("go", "run", path)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr

	return cmd.Run()
}

func main() {
	var day int
	var err error

	if len(os.Args) > 1 {
		day, err = strconv.Atoi(os.Args[1])
		if err != nil {
			fmt.Println("Usage: go run main.go [day]")
			os.Exit(1)
		}
	} else {
		day, err = getTodayDay()
		if err != nil {
			fmt.Println(err)
			os.Exit(1)
		}
	}

	fmt.Printf("Running Advent of Code 2025 Day %02d\n", day)

	if err := runDay(day); err != nil {
		fmt.Println("ERROR:", err)
		os.Exit(1)
	}
}
