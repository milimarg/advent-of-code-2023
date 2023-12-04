#!/bin/bash

total=0

cat "./input.txt" | \
while read -r line; do
  IFS=';' read -ra elements <<< "$line"
  greatest_red=0
  greatest_green=0
  greatest_blue=0
  for element in "${elements[@]}"; do
    echo "$element"
    red=$(echo "$element" | grep -Eo "[0-9]+ red" | cut -d ' ' -f1)
    red=$((red+0))
    green=$(echo "$element" | grep -Eo "[0-9]+ green" | cut -d ' ' -f1)
    green=$((green+0))
    blue=$(echo "$element" | grep -Eo "[0-9]+ blue" | cut -d ' ' -f1)
    blue=$((blue+0))
    if [[ $red -gt $greatest_red ]]; then
      greatest_red=$red
    fi
    if [[ $green -gt $greatest_green ]]; then
      greatest_green=$green
    fi
    if [[ $blue -gt $greatest_blue ]]; then
      greatest_blue=$blue
    fi
  done
  printf "greatest_red = %s\n" $greatest_red
  printf "greatest_green = %s\n" $greatest_green
  printf "greatest_blue = %s\n" $greatest_blue
  power=$((greatest_red*greatest_green*greatest_blue))
  total=$((total+power))
  printf "total = %s\n\n" $total
done
