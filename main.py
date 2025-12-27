from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

while True:
    text = input("calc > ")
    if text.strip() == "":
        continue

    lexer = Lexer(text)
    tokens = lexer.generate_tokens()

    parser = Parser(tokens)
    tree = parser.expr()

    interpreter = Interpreter()
    result = interpreter.visit(tree)

    print(result)
