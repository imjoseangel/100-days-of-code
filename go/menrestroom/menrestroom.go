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
var untaken []int
var taken []int
var timePeeing int
var newStall int
var left []int
var right []int
var stall int
var stallPrint string

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

func init() {

	rand.Seed(time.Now().UnixNano())
	timePeeing = rand.Intn(maxtimepeeing-mintimepeeing+1) + mintimepeeing
	untaken = makeRange(1, stalls)
	newStall = int(math.Floor(float64(sumArray(untaken)) / float64(len(untaken))))
	if stalls%2 == 0 {
		left = sliceArray(untaken[0:newStall-1], 0)
	} else {
		left = sliceArray(untaken[0:newStall-1], 1)
	}
	right = sliceArray(untaken[newStall:], 1)
	stallPrint = strings.Repeat(emoEmpty, stalls) + emoDoor

}

func takeStall() {
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
		taken = append(taken, stall)
	}
}
func main() {

	takeStall()
	fmt.Println(stallPrint)

}
