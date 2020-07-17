package main

import "oop/employee"

func main() {
	e := employee.New("Sam", "Adolf", 30, 20)
	// e:= employee.Employee {
	// 	FirstName: "Sam",
	// 	LastName: "Adolf",
	// 	TotalLeaves: 30,
	// 	LeavesTaken: 20,
	// }
	e.LeavesRemaining()
}
