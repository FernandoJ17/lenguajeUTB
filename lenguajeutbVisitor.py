# Generated from C:/Users/GERMAN/PycharmProjects/ANTLR\lenguajeutb.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .lenguajeutbParser import lenguajeutbParser
else:
    from lenguajeutbParser import lenguajeutbParser

# This class defines a complete generic visitor for a parse tree produced by lenguajeutbParser.

class lenguajeutbVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by lenguajeutbParser#start_rule.
    def visitStart_rule(self, ctx:lenguajeutbParser.Start_ruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeutbParser#principal.
    def visitPrincipal(self, ctx:lenguajeutbParser.PrincipalContext):
        operador = None
        primera_iteracion = True
        resultado = None
        for child in ctx.getChildren():
            if primera_iteracion:
                primera_iteracion = False
                resultado = int(child.getText())
            else:
                if child.getText() == "/" or child.getText() == "*":
                    operador = child.getText()
                else:
                    lado_derecho = (child.getText())
                    if operador == "/":
                        resultado //= lado_derecho
                    else:
                        resultado *= lado_derecho
        return resultado


    # Visit a parse tree produced by lenguajeutbParser#bloques.
    def visitBloques(self, ctx:lenguajeutbParser.BloquesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeutbParser#flujo.
    def visitFlujo(self, ctx:lenguajeutbParser.FlujoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeutbParser#variables.
    def visitVariables(self, ctx:lenguajeutbParser.VariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeutbParser#declaracion.
    def visitDeclaracion(self, ctx:lenguajeutbParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeutbParser#sentencias.
    def visitSentencias(self, ctx:lenguajeutbParser.SentenciasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeutbParser#imprimir.
    def visitImprimir(self, ctx:lenguajeutbParser.ImprimirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeutbParser#comentario.
    def visitComentario(self, ctx:lenguajeutbParser.ComentarioContext):
        return self.visitChildren(ctx)



del lenguajeutbParser