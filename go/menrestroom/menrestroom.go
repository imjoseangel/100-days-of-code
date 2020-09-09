///bin/true; exec /usr/bin/env go run "" "$@"
package main

import (
	"fmt"
	"math"
	"math/rand"
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

func sum(array []int) int {
	result := 0
	for _, value := range array {
		result += value
	}
	return result
}

func takeStall() {

	rand.Seed(time.Now().UnixNano())
	timepeeing := rand.Intn(maxtimepeeing-mintimepeeing+1) + mintimepeeing
	untaken := makeRange(1, stalls)
	taken := make([]int, stalls)
	newStall := math.Floor(float64(sum(untaken)) / float64(len(untaken)))
	fmt.Println(emoDoor, emoEmpty, emoTaken, timepeeing, taken, newStall)
}

func main() {

	takeStall()
}
