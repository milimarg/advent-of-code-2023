// 253473930

// TODO: REPLACE STRUCT 2 ELEMENTS BY MAP

package main

import (
	"slices"
	"strings"
)

func runTask02(hand string, len int, cardValues map[string]int) int {
	if strings.Contains(hand, "J") {
		temp := make([]int, 0)
		for key := range cardValues {
			if key == "J" {
				continue
			}
			replacedHand := strings.Replace(hand, "J", key, -1)
			temp = append(temp, getStrengthOfHand(replacedHand, len))
		}
		return slices.Max(temp)
	} else {
		return getStrengthOfHand(hand, len)
	}
}
