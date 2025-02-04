use std::fmt;

use miette::Error;

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub enum Token<'a> {
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
    Literal(&'a str),
}
//output the result that we were looking for
impl fmt::Display for Token<'_> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(
            f,
            "{}",
            match self {
                Token::LeftParen => "LEFT_PAREN",
                Token::RightParen => "RIGHT_PAREN",
                Token::LeftBrace => "LEFT_BRACE",
                Token::RightBrace => "RIGHT_BRACE",
                Token::COMMA => "COMMA",
                Token::MINUS => "MINUS",
                Token::PLUS => "PLUS",
                Token::STAR => "STAR",
                Token::DOT => "DOT",
                Token::SEMICOLON => "SEMICOLON",
                Token::Literal(_) => todo!(),
            }
        )
    }
}

pub struct Lexer<'a> {
    rest: &'a str,
}

impl<'a> Lexer<'a> {
    pub fn new(input: &'a str) -> Self {
        Self { rest: input }
    }
}

impl<'a> Iterator for Lexer<'a>
where
    T: Iterator<Item = char>,
{
    type Item = Result<Token<'a>, Error>;

    fn next(&mut self) -> Option<Self::Item> {
        //actual lexing happens here
        //figure out the next output token for the stream
        //and going to depend on what the inputs are.
        // let c = self.iterator.next()?;
        //pull out the first character of string and return the first item of the Option
        let c = self.rest.chars().next()?;
        // reassign rest to bump on the nxt of rest.
        self.rest = &self.rest[c.len_utf8()..];

        match c {
            //construct up
            // add add these as variants
            '(' => return Some(Ok(Token::LeftParen)),
            ')' => return Some(Ok(Token::RightParen)),
            '{' => return Some(Ok(Token::LeftBrace)),
            '}' => return Some(Ok(Token::RightBrace)),
            ',' => return Some(Ok(Token::COMMA)),
            '-' => return Some(Ok(Token::MINUS)),
            '.' => return Some(Ok(Token::DOT)),
            '+' => return Some(Ok(Token::PLUS)),
            ';' => return Some(Ok(Token::SEMICOLON)),
            '*' => return Some(Ok(Token::STAR)),
            _ => panic!("Token doesn't exist!"),
        };
    }
}

//once the iterator returns `Err`, it will only return `None`
// grabbing character from the input, when succesffuly yield them ,
// we return them , or we end up with a lexing error ,
// make the iterator then return the error , then the iterator is sort of invalidated.
pub fn lex(input: impl IntoIterator<Item = char>) -> impl Iterator<Item = Result<Token, Error>> {
    Lexer::new(input)
}
