# Generated from C:/Users/juanp/PycharmProjects/lenguajeUTB\lenguajeutb.g4 by ANTLR 4.7
from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
if __name__ is not None and "." in __name__:
    from .lenguajeutbParser import lenguajeutbParser
else:
    from lenguajeutbParser import lenguajeutbParser

# This class defines a complete generic visitor for a parse tree produced by lenguajeutbParser.

class lenguajeutbVisitor(ParseTreeVisitor):
    tabla_de_simbolos = {}
    # Visit a parse tree produced by lenguajeutbParser#start_rule.
    def visitStart_rule(self, ctx:lenguajeutbParser.Start_ruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeutbParser#nombre_programa.
    def visitNombre_programa(self, ctx:lenguajeutbParser.Nombre_programaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeutbParser#variables.
    def visitVariables(self, ctx:lenguajeutbParser.VariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeutbParser#flujo.
    def visitFlujo(self, ctx:lenguajeutbParser.FlujoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeutbParser#sentencias.
    def visitSentencias(self, ctx:lenguajeutbParser.SentenciasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeutbParser#asignacion.
    def visitAsignacion(self, ctx:lenguajeutbParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeutbParser#ciclo_para.
    def visitCiclo_para(self, ctx:lenguajeutbParser.Ciclo_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeutbParser#ciclo_mientras.
    def visitCiclo_mientras(self, ctx:lenguajeutbParser.Ciclo_mientrasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeutbParser#si.
    def visitSi(self, ctx:lenguajeutbParser.SiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeutbParser#expresion.
    def visitExpresion(self, ctx:lenguajeutbParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeutbParser#div.
    def visitDiv(self, ctx:lenguajeutbParser.DivContext):
        resultado, operador, primera_iteracion = None, None, True
        for hijo in ctx.children:
            if first_iter:
                first_iter = False
                resultado = self.visit(hijo)
            elif type(hijo) == TerminalNodeImpl:
                operator = hijo.getText()
            else:
                segundo_operando = self.visit(hijo)
                # TODO al momento de traducir hay que convertir el operando correspondiente
                if resultado != segundo_operando:
                    if resultado == int:
                        if segundo_operando == float:
                            resultado = float
                        elif segundo_operando == bool:
                            segundo_operando = int
                        else:
                            raise ValueError
                    elif resultado == bool:
                        if segundo_operando == int:
                            resultado = int
                        else:
                            raise ValueError
                    elif resultado == float:
                        if segundo_operando == int:
                            segundo_operando = float
                        else:
                            raise ValueError
                    else:
                        raise ValueError
                if operador == "/":
                    pass
                else:
                    pass


    # Visit a parse tree produced by lenguajeutbParser#atom.
    def visitAtom(self, ctx:lenguajeutbParser.AtomContext):
        if ctx.e is not None:
            return int
        elif ctx.t is not None:
            return str
        elif ctx.r is not None:
            return float
        elif ctx.exp is not None:
            return ctx.visit(ctx.exp)
        elif ctx.iden is not None:
            if ctx.iden.text not in lenguajeutbVisitor.tabla_de_simbolos:
                raise Exception
            else:
                return lenguajeutbVisitor.tabla_de_simbolos[ctx.iden.text]
        else:
            return  ctx.visit(ctx.conv)


    # Visit a parse tree produced by lenguajeutbParser#conversion.
    def visitConversion(self, ctx:lenguajeutbParser.ConversionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeutbParser#acceso_lista.
    def visitAcceso_lista(self, ctx:lenguajeutbParser.Acceso_listaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeutbParser#acceso_matriz.
    def visitAcceso_matriz(self, ctx:lenguajeutbParser.Acceso_matrizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeutbParser#imprimir.
    def visitImprimir(self, ctx:lenguajeutbParser.ImprimirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lenguajeutbParser#s.
    def visitS(self, ctx:lenguajeutbParser.SContext):
        return self.visitChildren(ctx)



del lenguajeutbParser