///bin/true; exec /usr/bin/env go run "" "$@"
package main

var stalls int = 10
var stallfreq int = 2
var mintimepeeing int = 1
var maxtimepeeing int = 10

func makeRange(min, max int) []int {
	a := make([]int, max-min+1)
	for i := range a {
		a[i] = min + i
	}
	return a
}

func takeStall() {

	untaken := makeRange(1, stalls)
	taken := make([]int, stalls)
}

func main() {

}
