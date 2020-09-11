///bin/true; exec /usr/bin/env go run "" "$@"
package main

import (
	"fmt"
	"math"
	"math/rand"
	"strings"
	"time"
)

var stalls int = 10
var stallfreq int = 2
var mintimepeeing int = 1
var maxtimepeeing int = 10

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

func initVars() {

	rand.Seed(time.Now().UnixNano())
	timePeeing := rand.Intn(maxtimepeeing-mintimepeeing+1) + mintimepeeing
	untaken := makeRange(1, stalls)
	taken := make([]int, stalls)
	newStall := int(math.Floor(float64(sumArray(untaken)) / float64(len(untaken))))
	left := []int{}
	if stalls%2 == 0 {
		left = sliceArray(untaken[0:newStall-1], 0)
	} else {
		left = sliceArray(untaken[0:newStall-1], 1)
	}
	right := sliceArray(untaken[newStall:], 1)
	stallPrint := strings.Repeat(emoEmpty, stalls) + emoDoor

	fmt.Println(emoDoor, emoEmpty, emoTaken, timePeeing, taken, newStall, left, right, stallPrint)
}

func main() {

	initVars()
}
