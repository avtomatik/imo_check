fn is_valid_imo(mut value: u32) -> bool {
    let mut numbers = Vec::with_capacity(7);

    for _ in 0..7 {
        let number = value % 10;
        value /= 10;
        numbers.push(number);
    }

    let number = numbers.remove(0);

    let sum: u32 = numbers.iter()
                           .zip(2..8)
                           .map(|(&x, y)| x * y)
                           .sum();

    sum % 10 != number
}

fn main() {
    let value = 9000003; // Example value
    let result = is_valid_imo(value);
    println!("{}", result);
}
