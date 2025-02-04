use std::fmt;

use miette::{Error, WrapErr};

pub enum Token {
    LeftParen,
    RightParen,
    LeftBrace,
    RightBrace,
    COMMA,
    DOT,
    MINUS,
    PLUS,
    SEMICOLON,
    STAR,
}
impl fmt::Display for Token {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}", 
        match self {Token::LeftParen=>"LEFT PAREN",Token::RightParen=>"RIGHT PAREN",Token::LeftBrace=>"LEFT BRACE",Token::RightBrace=>"RIGHT BRACE",Token::COMMA=>"COMMA",Token::MINUS=>"MINUS",Token::PLUS=>"PLUS",Token::STAR=>"STAR",
            Token::DOT => "DOT",
            Token::SEMICOLON => "SEMICOLON", })
    }
}


pub struct Lexer<T> {
    iterator: T,
}

impl<T> Lexer<T> {
    pub fn new(input: impl IntoIterator<Item = char, IntoIter = T>) -> Self {
        Self {
            iterator: input.into_iter(),
        }
    }
}

impl<T> Iterator for Lexer<T>
where
    T: Iterator<Item = char>,
{
    type Item = Result<Token, Error>;

    fn next(&mut self) -> Option<Self::Item> {
        //figure out the next token
        while let Some(c) = self.iterator.next() {
            let c = self.iterator.next()?;
            match c {
                //construct up
                '(' =>return Some(Token::LeftParen),
                ')' =>return Some(Token::RightParen),,
                '{' =>return Some(Token::LeftBrace),
                '}' =>return Some(Token::RightBrace),
                ',' =>return Some(Token::COMMA),
                '-' =>return Some(Token::MINUS),
                '.' =>return Some(Token::DOT),
                '+' =>return Some(Ok(Token::PLUS)),
                ';' =>return Some(Token::SEMICOLON),
                '*' =>return Some(Token::STAR),
            }
        }
    }
}

//once the iterator returns `Err`, it will only return `None`
pub fn lex(input: impl IntoIterator<Item = char>) -> impl Iterator<Item = Result<Token, Error>> {
    Lexer::new(input)
}
