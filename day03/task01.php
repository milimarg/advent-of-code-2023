<?php

ini_set('display_errors', '1');
ini_set('display_startup_errors', '1');
error_reporting(E_ALL);

$file = file_get_contents('./input.txt', true);

$array = explode("\n", $file);
$array_len = count($array);

function is_char_a_symbol($char) {
    return !is_numeric($char) && $char != '.';
}

function parse_number($array, $x, $y, $len) {
    $number = 0;
    for ($i = 0; $i < $len; $i++) {
        $char = $array[$y][$x + $i];
        $number = $number * 10 + ($char - '0');
    }
    return $number;
}

function check_number_around($array, $y, $x, $number_len, $array_len, $len) {
    $start_x = $x - 1;
    $start_y = $y - 1;
    
    for ($offset_y = 0; $offset_y < 3; $offset_y++) {
        for ($offset_x = 0; $offset_x < $number_len + 2; $offset_x++) {
            if ($start_y + $offset_y < 0 ||
                $start_y + $offset_y >= $array_len ||
                $start_x + $offset_x < 0 ||
                $start_x + $offset_x >= $len) {
                continue;
            }
            if (is_char_a_symbol($array[$start_y + $offset_y][$start_x + $offset_x])) {
                return 1;
            }
        }
    }
    return 0;
}

$sum = 0;

for ($y = 0; $y < $array_len; $y++) {
    $len = strlen($array[$y]);
    for ($x = 0; $x < $len; $x++) {
        $current_element = $array[$y][$x];
        $number_len = 0;
        if (!is_numeric($current_element)) {
            continue;
        }
        while (is_numeric($current_element) && $x + $number_len < $len) {
            $current_element = $array[$y][$x + $number_len];
            $number_len++;
        }
        $valid = check_number_around($array, $y, $x, $number_len - 1, $array_len, $len);
        if ($valid) {
            if ($x + $number_len == $len && is_numeric($current_element)) {
                $number_len++;
            }
            $sum += parse_number($array, $x, $y, $number_len - 1);
        }
        $x += $number_len - 1;
    }
}

echo "sum = $sum<br>";
