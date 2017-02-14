package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	file, err := os.Open("large.in")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	scanner.Scan()
	testCase := 1
	for scanner.Scan() {
		words := strings.Split(scanner.Text(), " ")
		result := ""
		sep := ""
		for i := len(words) - 1; i >= 0; i-- {
			result += sep
			result += words[i]
			sep = " "
		}
		caseString := fmt.Sprintf("Case #%d: %s\n", testCase, result)
		fmt.Printf(caseString)
		testCase++
	}
}
