from .ast_ import *

def concat(*a):
    return ''.join(a)

def code(ast):
    # code, header_list = translate(ast)

    code = "#include <stdio.h>\n\n"
    code = concat(code, "int main(void)")
    code = concat(code, translate(ast))
    return code



def translate(ast, indent=0):
    code = "\t" * indent
    if type(ast) is Block:
        code = " {\n"
        for obj in ast.bodys:
            code = concat(code, translate(obj, indent+1), '\n')
        code = concat(code, "\t" * indent, "}")
    elif type(ast) is Define:
        code = concat(code, f"int {translate(ast.left, indent)} = {translate(ast.right, indent)};")
    elif type(ast) is Print:
        code = concat(code, f'printf("%d\\n", {translate(ast.value, indent)});')
    elif type(ast) is Function:
        pass
    elif type(ast) is If:
        code = concat(code, f"if ({translate(ast.expr, indent)})")
        code = concat(code, translate(ast.block, indent), " else")
        code = concat(code, translate(ast.other, indent))
    elif issubclass(ast, BinaryOperator):
        bin_op_list = {
            Add: '+',
            Sub: '-',
            Mul: '*',
            Div: '/',
            Lessthan: '<',
            Greaterthan: '>',
            LessthanEqual: '<=',
            GreaterthanEqual: '>=',
            Equal: '==',
            NotEqual: '!=',
            And: '&&',
            Or: '||'
        }
        code = f"{translate(ast.left, indent)} {bin_op_list[type(ast)]} {translate(ast.right, indent)}"
    elif type(ast) is Number:
        code = f"{ast.value}"
    elif type(ast) is Identifier:
        code = f"{ast.name}"

    return code