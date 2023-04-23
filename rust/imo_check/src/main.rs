/*
fn is_valid_imo(arr: Vec<&str>) -> bool {
TODO: Implement Function
}
*/

fn main() {
    let imo = "9000003";
    for (idx, c) in imo.chars().rev().enumerate().skip(1) {
        println!("{} {}", 1 + idx, c);
    }
}
