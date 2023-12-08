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

	for i := 1; i < 3; i++ {
		file, err := os.Open("./input.txt")
		if err != nil {
			log.Fatal(err)
		}

		scanner := bufio.NewScanner(file)

		if err := scanner.Err(); err != nil {
			log.Fatal(err)
		}

		if i == 2 {
			cardValues["J"] = 1
		}

		hands := make([]hand, 0)
		for scanner.Scan() {
			line := scanner.Text()
			split := strings.Split(line, " ")
			handPart := split[0]
			bidPart := split[1]
			strength := 0
			handLen := len(handPart)

			if i == 2 {
				strength = runTask02(handPart, handLen, cardValues)
			} else {
				strength = getStrengthOfHand(handPart, handLen)
			}

			bidInt, bidError := strconv.Atoi(bidPart)
			if bidError != nil {
				panic(bidError)
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

		fmt.Println("part", i, "; total =", total)
		file.Close()
	}
}
