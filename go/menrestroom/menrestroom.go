///bin/true; exec /usr/bin/env go run "" "$@"
package main

import (
	"fmt"
	"math"
	"math/rand"
	"sort"
	"strings"
	"time"
)

var untaken []int
var taken []int
var timePeeing time.Duration
var newStall int
var left []int
var right []int
var stall int
var stallPrint []string

const stalls int = 10
const stallFreq time.Duration = 1
const mintimepeeing int = 1
const maxtimepeeing int = 10
const emoEmpty string = "\U0001F6BD"
const emoTaken string = "\U0001F6B6"
const emoDoor string = "\U0001F6AA"
const halfValue float32 = 0.5

func makeRange(min, max int) []int {
	a := make([]int, max-min+1)
	for i := range a {
		a[i] = min + i
	}
	return a
}

func sumArray(array []int) int {
	result := 0
	for _, numb := range array {
		result += numb
	}
	return result
}

func sliceArray(array []int, start int) []int {

	result := []int{}
	for i := start; i < len(array); i += 2 {
		result = append(result, array[i])
	}
	return result
}

func index(slice []int, item int) int {
	for result := range slice {
		if slice[result] == item {
			return result
		}
	}
	return -1
}

func init() {

	rand.Seed(time.Now().UnixNano())
	timePeeing = time.Duration(rand.Intn(maxtimepeeing-mintimepeeing+1) + mintimepeeing)
	untaken = makeRange(1, stalls)
	newStall = int(math.Floor(float64(sumArray(untaken)) / float64(len(untaken))))
	if stalls%2 == 0 {
		left = sliceArray(untaken[0:newStall-1], 0)
	} else {
		left = sliceArray(untaken[0:newStall-1], 1)
	}
	right = sliceArray(untaken[newStall:], 1)
	stallPrint = strings.SplitN(strings.Repeat(emoEmpty, stalls)+emoDoor, "", stalls+1)

}

func takeStall() []string {

	if len(untaken) > 0 {
		if len(taken) == 0 {
			stall = newStall
		} else {
			if len(left) > 0 {
				randomIndex := rand.Intn(len(left))
				stall = left[randomIndex]
				left = append(left[:randomIndex], left[randomIndex+1:]...)
			} else if len(right) > 0 {
				randomIndex := rand.Intn(len(right))
				stall = right[randomIndex]
				right = append(right[:randomIndex], right[randomIndex+1:]...)

			} else {
				randomIndex := rand.Intn(len(untaken))
				stall = untaken[randomIndex]
			}
		}
		stallIndex := index(untaken, stall)
		untaken = append(untaken[:stallIndex], untaken[stallIndex+1:]...)
	}

	taken = append(taken, stall)

	stallPrint[taken[len(taken)-1]-1] = emoTaken

	// leaveTimer := time.NewTimer(timePeeing)
	// <-leaveTimer.C
	// time.Sleep(timePeeing)
	leaveTimer := time.NewTimer(timePeeing * time.Second)

	select {
	case <-leaveTimer.C:
		leaveStall()
	}

	return stallPrint
}

func leaveStall() {

	if len(taken) > 0 {
		oldStall := taken[0]
		taken = append(taken[:0], taken[1:]...)
		untaken = append(untaken, oldStall)
		sort.Ints(untaken)
		stallPrint[oldStall-1] = emoEmpty
		timePeeing = time.Duration(rand.Intn(maxtimepeeing-mintimepeeing+1) + mintimepeeing)
	}

	return
}

func main() {

	//takeTicker := time.NewTicker(stallFreq * time.Second)
	//leaveTicker := time.NewTicker(timePeeing)

	for len(untaken) > 0 {
		fmt.Println("\033[H\033[2J")

		for _, item := range stallPrint {
			fmt.Print(item + " ")

		}

		takeTimer := time.NewTimer(stallFreq * time.Second)

		select {
		case <-takeTimer.C:
			go takeStall()
		}

		//time.Sleep(stallFreq * time.Second)

		//go takeStall()
		//go leaveStall()

	}

	fmt.Println("\033[H\033[2J")
	for _, item := range stallPrint {
		fmt.Print(item + " ")
	}

	fmt.Println()

}
