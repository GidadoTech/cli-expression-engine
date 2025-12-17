from lexer import Lexer

text = input("expr> ")
lexer = Lexer(text)

while True:
    token = lexer.get_next_token()
    print(token)
    if token.type.name == "EOF":
        break
