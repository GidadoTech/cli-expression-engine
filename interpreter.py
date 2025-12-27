class Interpreter:
    def visit(self, node):
        method_name = f"visit_{type(node).__name__}"
        method = getattr(self, method_name, self.no_visit_method)
        return method(node)

    def no_visit_method(self, node):
        raise Exception(f"No visit method for {type(node).__name__}")

    def visit_NumberNode(self, node):
        return node.token.value

    def visit_BinOpNode(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)

        if node.op_token.type.name == "PLUS":
            return left + right
        if node.op_token.type.name == "MINUS":
            return left - right
        if node.op_token.type.name == "MUL":
            return left * right
        if node.op_token.type.name == "DIV":
            return left / right
