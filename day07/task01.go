// 253933213

package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

type matchLetter struct {
	letter rune
	number int
}

type hand struct {
	handContent string
	bid         int
	strength    int
}

type order struct {
	name  rune
	value int
}

func isStringInSlice(str int, list []int) bool {
	for _, listStr := range list {
		if listStr == str {
			return true
		}
	}
	return false
}

func isCharFound(str rune, list []matchLetter) bool {
	for _, element := range list {
		if element.letter == str {
			return true
		}
	}
	return false
}

func incrementLetter(list []matchLetter, char rune) int {
	for index, element := range list {
		if element.letter == char {
			return index
		}
	}
	return -1
}

func getStrongestHand(hand1 string, hand2 string, cardValues map[string]int) *string {
	for i := range hand1 {
		char1 := string(string(hand1)[i])
		char2 := string(string(hand2)[i])
		if int(cardValues[char1]) > int(cardValues[char2]) {
			return &hand1
		}
		if int(cardValues[char1]) < int(cardValues[char2]) {
			return &hand2
		}
	}
	return nil
}

func getStrengthOfHand(hand string, handLen int) int {
	matchesLetter := make([]matchLetter, 0)
	strength := 0
	for index, char := range hand {
		temp := make([]int, 0)
		for index2, char2 := range hand {
			if index != index2 && char == char2 && isStringInSlice(index, temp) == false {
				temp = append(temp, index)
				if isCharFound(char2, matchesLetter) == false {
					matchesLetter = append(matchesLetter, matchLetter{
						letter: char2,
						number: 1,
					})
				} else {
					searchIndex := incrementLetter(matchesLetter, char2)
					if searchIndex != -1 {
						matchesLetter[searchIndex].number += 1
					}
				}
			}
		}
	}
	len := len(matchesLetter)
	if len == 1 && matchesLetter[0].number == 2 {
		strength = 1
	}
	if len == 2 {
		if matchesLetter[0].number+matchesLetter[1].number == handLen {
			strength = 4
		} else {
			strength = 2
		}
	}
	if len == 1 && matchesLetter[0].number == 3 {
		strength = 3
	}
	if len == 1 && matchesLetter[0].number == 4 {
		strength = 5
	}
	if len == 1 && matchesLetter[0].number == 5 {
		strength = 6
	}
	return strength
}

func main() {
	cardValues := map[string]int{
		"2": 2,
		"3": 3,
		"4": 4,
		"5": 5,
		"6": 6,
		"7": 7,
		"8": 8,
		"9": 9,
		"T": 10,
		"J": 11,
		"Q": 12,
		"K": 13,
		"A": 14,
	}

	file, err := os.Open("./input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	hands := make([]hand, 0)
	for scanner.Scan() {
		line := scanner.Text()
		split := strings.Split(line, " ")
		handPart := split[0]
		bidPart := split[1]

		len := len(handPart)
		strength := getStrengthOfHand(handPart, len)

		bidInt, bidError := strconv.Atoi(bidPart)
		if bidError != nil {
			panic(err)
		}
		hands = append(hands, hand{
			handContent: handPart,
			bid:         bidInt,
			strength:    strength,
		})
	}

	sort.Slice(hands, func(p, q int) bool {
		return hands[p].strength < hands[q].strength
	})

	handLen := len(hands)
	for i := 0; i < handLen; i++ {
		for j := 0; j < handLen-i-1; j++ {
			hand1 := hands[j]
			hand2 := hands[j+1]
			if i != j && hand1.strength == hand2.strength {
				strongest := getStrongestHand(hand1.handContent, hand2.handContent, cardValues)
				if strongest == nil {
					continue
				}
				if *strongest == hand1.handContent {
					hands[j], hands[j+1] = hands[j+1], hands[j]
				}
			}
		}
	}

	total := 0
	for index, hand := range hands {
		total += int(hand.bid) * (index + 1)
	}

	fmt.Println("total = ", total)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
