use std::env;
use std::fs;
use std::process;
fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() > 1 {
        println!("Usage: lox [script]");
        process::exit(64);
    } else if args.len() == 1 {
        run_file(&args[0]);
    } else {
        run_prompt();
    }
}

fn run_file(path: &String) {
    let data = fs::read_to_string(path).expect("Failed to read the file");
    run(data);
}

fn run_prompt() {
    
}
