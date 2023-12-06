use std::fs;

fn main() {
    let file_contents = fs::read_to_string("./input.txt")
        .expect("file should've been open");
    let splitted_file = file_contents.split("\n");

    let mut result = 1;
    let mut line_index = 0;
    let mut time_vec: Vec<i64> = Vec::new();
    let mut distance_vec: Vec<i64> = Vec::new();

    for line in splitted_file {
        if let Some(splitted_line) = line.split(":").nth(1) {
            let numbers = splitted_line.split(" ");
            for number in numbers {
                if !number.parse::<i64>().is_ok() {
                    continue;
                }
                match number.parse() {
                    Ok(number) => {
                        if line_index == 0 {
                            time_vec.push(number);
                        } else {
                            distance_vec.push(number);
                        }
                    },
                    Err(_) => ()
                }
            }
        } else {
            println!("oh no problem with splitted_line");
        }
        line_index += 1;
    }

    for (time, distance) in time_vec.iter().zip(distance_vec.iter()) {
        let mut tries_number = 0;

        for i in 1..*time {
            if (time - i) * i > *distance {
                tries_number += 1;
            }
        }
        println!("time = {} ; tries = {}", time, tries_number);
        result *= tries_number;
    }
    println!("sum = {}", result);
}

// to do task 2, just concatenate manually all races