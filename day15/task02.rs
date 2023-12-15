use std::fs::File;
use std::io::{self, Read};

fn main() -> io::Result<()> {
    let file_path = "input.txt";
    let mut file = File::open(file_path)?;
    let mut buffer = String::new();

    file.read_to_string(&mut buffer)?;

    let parts = buffer.split(",");

    let mut sum = 0;

    for part in parts {
        let mut temp_sum = 0 as u32;
        let mut part_to_take = part;

        if part_to_take.contains("=") {
            let splitted: Vec<&str> = part_to_take.split('=').collect();

            if let Some(splitted_value) = splitted.get(0) {
                part_to_take = splitted_value;
            }
        }

        for char in part_to_take.chars() {
            let ascii = char as u8;
            temp_sum += ascii as u32;
            temp_sum *= 17;
            temp_sum %= 256;
        }
        println!("'{}' hash = {}", part_to_take, temp_sum);



        sum += temp_sum;
    }

    println!("END... {}", sum);

    Ok(())
}
