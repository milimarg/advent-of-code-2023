<?php

ini_set('display_errors', '1');
ini_set('display_startup_errors', '1');
error_reporting(E_ALL);

$file = file_get_contents('./input.txt', true);

$array = explode("\n", $file);
$array_len = count($array);

$sum = 0;

$known_stars = array();

function is_char_a_symbol($char) {
    return !is_numeric($char) && $char != '.';
}

function parse_number($array, $x, $y, $len) {
    $number = 0;
    echo "LEN = $len<br>";
    for ($i = 0; $i < $len; $i++) {
        $char = $array[$y][$x + $i];
        if (is_numeric($char)) {
            echo "char: '$char' ";
            $number = $number * 10 + ($char - '0');
        }
    }
    return $number;
}

function check_number_around($array, $y, $x, $number_len, $array_len, $len, &$known_stars) {
    $start_x = $x - 1;
    $start_y = $y - 1;
    $ayya = $number_len;
    
    for ($offset_y = 0; $offset_y < 3; $offset_y++) {
        for ($offset_x = 0; $offset_x < $ayya + 2; $offset_x++) {
            $temp_x = $start_x + $offset_x;
            $temp_y = $start_y + $offset_y;
            if ($temp_y < 0 ||
                $temp_y >= $array_len ||
                $temp_x < 0 ||
                $temp_x >= $len) {
                continue;
            }
            $char = $array[$temp_y][$temp_x];
            if (is_char_a_symbol($char) && $char == '*') {
                $key = "$temp_y $temp_x";
                if (!array_key_exists($key, $known_stars)) {
                    $known_stars[$key] = [];
                }
                array_push($known_stars[$key], $x, $y, $number_len);
                return 1;
            }
        }
    }
    return 0;
}

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
        check_number_around($array, $y, $x, $number_len - 1, $array_len, $len, $known_stars);
        $x += $number_len - 1;
    }
}

foreach ($known_stars as $key => $value) {
    $parts_number = 3;
    $value_len = count($value);
    if ($value_len != $parts_number * 2) {
        continue;
    }

    $ratio = 1;
    for ($i = 0; $i < $value_len; $i += $parts_number) {
        $x = $value[$i];
        $y = $value[$i + 1];
        $number_len = $value[$i + 2];
        $len = strlen($array[$y]);
        echo $x, " ", $number_len, " ", $len, "<br>";
        /*
         * if ($x + $number_len == $len && is_numeric($array[$y][$x])) {
            $number_len++;
        }
         */
        if ($x + $number_len == $len - 1 && is_numeric($array[$y][$x])) {
            $number_len++;
        }
        $number = parse_number($array, $x, $y, $number_len);
        echo "$number <br>";
        $ratio *= $number;
    }

    echo "=> ratio = $ratio";

    $sum += $ratio;

    echo "<br><br><br>";
}

echo "sum = $sum<br>";
