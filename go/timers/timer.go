///bin/true; exec /usr/bin/env go run "" "$@"
package main

import (
	"fmt"
	"log"
	"os/exec"
	"time"
)

var out []byte

func run(cmd string) []byte {
	out, err := exec.Command(cmd).Output()

	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(out)
	return out
}

func main() {

	uptimeTicker := time.NewTicker(2 * time.Second)
	dateTicker := time.NewTicker(4 * time.Second)

	for {
		select {
		case <-uptimeTicker.C:
			run("uptime")
		case <-dateTicker.C:
			run("date")
		}
	}
}
