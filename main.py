from antlr4 import *
from ejemploLexer import ejemploLexer
from ejemploParser import ejemploParser
from ejemploVisitor import ejemploVisitor
if __name__ == '__main__':
    entrada = FileStream("entrada.txt")
    lexer = ejemploLexer(entrada)
    stream = CommonTokenStream(lexer)
    parser = ejemploParser(stream)
    tree = parser.start_rule()
    visitor = ejemploVisitor()
    print(visitor.visit(tree))


