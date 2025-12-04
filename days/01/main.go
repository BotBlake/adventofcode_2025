package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type Dial struct {
	pointer    int
	zeroStops  int
	zeroPassed int
}

func NewDial() *Dial {
	return &Dial{
		pointer: 50,
	}
}

func (d *Dial) Move(direction string, amount int) {
	p := d.pointer

	for amount > 0 {
		switch direction {
		case "R":
			p++
		case "L":
			p--
		}

		// Wrap around 0–99
		if p >= 100 {
			p = 0
		} else if p < 0 {
			p = 99
		}

		// Passed zero during movement
		if p == 0 {
			d.zeroPassed++
		}

		amount--
	}

	// Stopped at zero after full movement
	if p == 0 {
		d.zeroStops++
	}

	d.pointer = p
}

func (d *Dial) ZeroPassed() int {
	return d.zeroPassed
}

func (d *Dial) ZeroStopped() int {
	return d.zeroStops
}

func (d *Dial) Pointer() int {
	return d.pointer
}

func main() {
	file, err := os.Open("days/01/puzzle_input.txt")
	if err != nil {
		panic(err)
	}

	dial := NewDial()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			continue
		}
		dir := string(line[0])
		amt, err := strconv.Atoi(line[1:])
		if err != nil {
			panic(err)
		}
		dial.Move(dir, amt)
	}

	fmt.Println("----------SOLUTION DAY 01----------")
	fmt.Printf("Part1: Dial stopped at zero %d times.\n", dial.ZeroStopped())
	fmt.Printf("Part2: Dial passed zero %d times.\n", dial.ZeroPassed())
	fmt.Println("-----------------------------------")
}
