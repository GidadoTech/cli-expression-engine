from ast_nodes import NumberNode, BinOpNode
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos]

    def error(self):
        raise Exception("Invalid syntax")

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]

    def parse(self):
        return self.expr()

    def factor(self):
        token = self.current_token
        self.advance()
        return NumberNode(token)

    def term(self):
        node = self.factor()

        while self.current_token.type.name in ("MUL", "DIV"):
            op_token = self.current_token
            self.advance()
            node = BinOpNode(node, op_token, self.factor())

        return node

    def expr(self):
        node = self.term()

        while self.current_token.type.name in ("PLUS", "MINUS"):
            op_token = self.current_token
            self.advance()
            node = BinOpNode(node, op_token, self.term())

        return node

