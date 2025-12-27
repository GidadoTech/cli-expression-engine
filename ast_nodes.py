class AST:
    pass


class NumberNode(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

    def __repr__(self):
        return f"NumberNode({self.value})"


class BinOpNode(AST):
    def __init__(self, left, op_token, right):
        self.left = left
        self.op = op_token
        self.right = right

    def __repr__(self):
        return f"BinOpNode({self.left}, {self.op.type.name}, {self.right})"
