#!/bin/bash

# red not > 12
# green not > 13
# blue not > 14

total=0

cat "./input.txt" | \
while read -r line; do
  id=$(echo "$line" | grep -Eo "Game [0-9]{1,3}" | cut -d ' ' -f2)
  valid=1
  IFS=';' read -ra elements <<< "$line"
  for element in "${elements[@]}"; do
    echo "$element"
    red=$(echo "$element" | grep -Eo "[0-9]+ red" | cut -d ' ' -f1)
    red=$((red+0))
    green=$(echo "$element" | grep -Eo "[0-9]+ green" | cut -d ' ' -f1)
    green=$((green+0))
    blue=$(echo "$element" | grep -Eo "[0-9]+ blue" | cut -d ' ' -f1)
    blue=$((blue+0))
    if [[ $red -gt 12 ]]; then
      valid=0
    fi
    if [[ $green -gt 13 ]]; then
      valid=0
    fi
    if [[ $blue -gt 14 ]]; then
      valid=0
    fi
  done
  if [[ $valid -eq 1 ]]; then
      total=$((total+id))
      printf "the game '%s' has been successful (total = %s)\n\n" "$id" "$total"
  fi
done
