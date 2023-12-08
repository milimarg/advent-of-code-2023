package main

type matchLetter struct {
	letter rune
	number int
}

type hand struct {
	handContent string
	bid         int
	strength    int
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
