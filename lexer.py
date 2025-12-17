from tokens import Token, TokenType

class Lexer:
    def __init__(self, text):
        self.text = text
        self.position = 0
        self.current_char = self.text[self.position]

    def advance(self):
        self.position += 1
        if self.position >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.position]

    def get_next_token(self):
        # We will improve this step by step
        if self.current_char is None:
            return Token(TokenType.EOF)

        if self.current_char.isdigit():
            value = self.current_char
            self.advance()
            return Token(TokenType.NUMBER, int(value))

        if self.current_char == '+':
            self.advance()
            return Token(TokenType.PLUS)

        if self.current_char == '-':
            self.advance()
            return Token(TokenType.MINUS)

        if self.current_char == '*':
            self.advance()
            return Token(TokenType.MULTIPLY)

        if self.current_char == '/':
            self.advance()
            return Token(TokenType.DIVIDE)

        if self.current_char == '(':
            self.advance()
            return Token(TokenType.LPAREN)

        if self.current_char == ')':
            self.advance()
            return Token(TokenType.RPAREN)

        if self.current_char.isspace():
            self.advance()
            return self.get_next_token()

        raise Exception(f"Invalid character: {self.current_char}")
