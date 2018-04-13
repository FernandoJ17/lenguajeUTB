# Generated from C:/Users/GERMAN/PycharmProjects/ANTLR\lenguajeutb.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("J\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\7\3\30\n\3\f\3\16\3\33")
        buf.write("\13\3\3\3\3\3\3\3\3\3\3\4\3\4\6\4#\n\4\r\4\16\4$\3\5\3")
        buf.write("\5\7\5)\n\5\f\5\16\5,\13\5\3\5\3\5\3\6\3\6\7\6\62\n\6")
        buf.write("\f\6\16\6\65\13\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\5\bB\n\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\2\2\13\2")
        buf.write("\4\6\b\n\f\16\20\22\2\4\4\2\16\21\25\25\4\2\20\20\23\23")
        buf.write("\2F\2\24\3\2\2\2\4\31\3\2\2\2\6\"\3\2\2\2\b&\3\2\2\2\n")
        buf.write("/\3\2\2\2\f8\3\2\2\2\16A\3\2\2\2\20C\3\2\2\2\22F\3\2\2")
        buf.write("\2\24\25\5\4\3\2\25\3\3\2\2\2\26\30\5\22\n\2\27\26\3\2")
        buf.write("\2\2\30\33\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\34\3")
        buf.write("\2\2\2\33\31\3\2\2\2\34\35\7\3\2\2\35\36\7\22\2\2\36\37")
        buf.write("\5\6\4\2\37\5\3\2\2\2 #\5\b\5\2!#\5\n\6\2\" \3\2\2\2\"")
        buf.write("!\3\2\2\2#$\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%\7\3\2\2\2&*")
        buf.write("\7\4\2\2\')\5\16\b\2(\'\3\2\2\2),\3\2\2\2*(\3\2\2\2*+")
        buf.write("\3\2\2\2+-\3\2\2\2,*\3\2\2\2-.\7\5\2\2.\t\3\2\2\2/\63")
        buf.write("\7\6\2\2\60\62\5\f\7\2\61\60\3\2\2\2\62\65\3\2\2\2\63")
        buf.write("\61\3\2\2\2\63\64\3\2\2\2\64\66\3\2\2\2\65\63\3\2\2\2")
        buf.write("\66\67\7\7\2\2\67\13\3\2\2\289\7\b\2\29:\7\t\2\2:;\7\13")
        buf.write("\2\2;<\7\23\2\2<=\7\n\2\2=>\t\2\2\2>\r\3\2\2\2?B\5\20")
        buf.write("\t\2@B\5\22\n\2A?\3\2\2\2A@\3\2\2\2B\17\3\2\2\2CD\7\f")
        buf.write("\2\2DE\t\3\2\2E\21\3\2\2\2FG\7\r\2\2GH\7\20\2\2H\23\3")
        buf.write("\2\2\2\b\31\"$*\63A")
        return buf.getvalue()


class lenguajeutbParser ( Parser ):

    grammarFileName = "lenguajeutb.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Nombre_del_ejercicio'", "'Flujo'", "'fin_flujo'", 
                     "'variables'", "'fin_variables'", "'tipo'", "<INVALID>", 
                     "'valor_inicial'", "'nombre'", "'mostrar_en_pantalla'", 
                     "'Nota:'" ]

    symbolicNames = [ "<INVALID>", "NOMBRE_EJERCICIO", "FLUJO", "FIN_FLUJO", 
                      "VARIABLES", "FIN_VARIABLES", "TIPO", "TIPO_VARIABLE", 
                      "VALOR_INICIAL", "NOMBRE", "MOSTRAR", "NOTA", "ENTERO", 
                      "REAL", "STRING", "CHAR", "PALABRA", "IDENTIFICADOR", 
                      "WS", "BOOLEANO" ]

    RULE_start_rule = 0
    RULE_principal = 1
    RULE_bloques = 2
    RULE_flujo = 3
    RULE_variables = 4
    RULE_declaracion = 5
    RULE_sentencias = 6
    RULE_imprimir = 7
    RULE_comentario = 8

    ruleNames =  [ "start_rule", "principal", "bloques", "flujo", "variables", 
                   "declaracion", "sentencias", "imprimir", "comentario" ]

    EOF = Token.EOF
    NOMBRE_EJERCICIO=1
    FLUJO=2
    FIN_FLUJO=3
    VARIABLES=4
    FIN_VARIABLES=5
    TIPO=6
    TIPO_VARIABLE=7
    VALOR_INICIAL=8
    NOMBRE=9
    MOSTRAR=10
    NOTA=11
    ENTERO=12
    REAL=13
    STRING=14
    CHAR=15
    PALABRA=16
    IDENTIFICADOR=17
    WS=18
    BOOLEANO=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Start_ruleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def principal(self):
            return self.getTypedRuleContext(lenguajeutbParser.PrincipalContext,0)


        def getRuleIndex(self):
            return lenguajeutbParser.RULE_start_rule

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart_rule" ):
                return visitor.visitStart_rule(self)
            else:
                return visitor.visitChildren(self)




    def start_rule(self):

        localctx = lenguajeutbParser.Start_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start_rule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.principal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrincipalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOMBRE_EJERCICIO(self):
            return self.getToken(lenguajeutbParser.NOMBRE_EJERCICIO, 0)

        def PALABRA(self):
            return self.getToken(lenguajeutbParser.PALABRA, 0)

        def bloques(self):
            return self.getTypedRuleContext(lenguajeutbParser.BloquesContext,0)


        def comentario(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lenguajeutbParser.ComentarioContext)
            else:
                return self.getTypedRuleContext(lenguajeutbParser.ComentarioContext,i)


        def getRuleIndex(self):
            return lenguajeutbParser.RULE_principal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrincipal" ):
                return visitor.visitPrincipal(self)
            else:
                return visitor.visitChildren(self)




    def principal(self):

        localctx = lenguajeutbParser.PrincipalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_principal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==lenguajeutbParser.NOTA:
                self.state = 20
                self.comentario()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(lenguajeutbParser.NOMBRE_EJERCICIO)
            self.state = 27
            self.match(lenguajeutbParser.PALABRA)
            self.state = 28
            self.bloques()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BloquesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def flujo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lenguajeutbParser.FlujoContext)
            else:
                return self.getTypedRuleContext(lenguajeutbParser.FlujoContext,i)


        def variables(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lenguajeutbParser.VariablesContext)
            else:
                return self.getTypedRuleContext(lenguajeutbParser.VariablesContext,i)


        def getRuleIndex(self):
            return lenguajeutbParser.RULE_bloques

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloques" ):
                return visitor.visitBloques(self)
            else:
                return visitor.visitChildren(self)




    def bloques(self):

        localctx = lenguajeutbParser.BloquesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bloques)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [lenguajeutbParser.FLUJO]:
                    self.state = 30
                    self.flujo()
                    pass
                elif token in [lenguajeutbParser.VARIABLES]:
                    self.state = 31
                    self.variables()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 34 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==lenguajeutbParser.FLUJO or _la==lenguajeutbParser.VARIABLES):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FlujoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLUJO(self):
            return self.getToken(lenguajeutbParser.FLUJO, 0)

        def FIN_FLUJO(self):
            return self.getToken(lenguajeutbParser.FIN_FLUJO, 0)

        def sentencias(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lenguajeutbParser.SentenciasContext)
            else:
                return self.getTypedRuleContext(lenguajeutbParser.SentenciasContext,i)


        def getRuleIndex(self):
            return lenguajeutbParser.RULE_flujo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFlujo" ):
                return visitor.visitFlujo(self)
            else:
                return visitor.visitChildren(self)




    def flujo(self):

        localctx = lenguajeutbParser.FlujoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_flujo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(lenguajeutbParser.FLUJO)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==lenguajeutbParser.MOSTRAR or _la==lenguajeutbParser.NOTA:
                self.state = 37
                self.sentencias()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43
            self.match(lenguajeutbParser.FIN_FLUJO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariablesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLES(self):
            return self.getToken(lenguajeutbParser.VARIABLES, 0)

        def FIN_VARIABLES(self):
            return self.getToken(lenguajeutbParser.FIN_VARIABLES, 0)

        def declaracion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lenguajeutbParser.DeclaracionContext)
            else:
                return self.getTypedRuleContext(lenguajeutbParser.DeclaracionContext,i)


        def getRuleIndex(self):
            return lenguajeutbParser.RULE_variables

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables" ):
                return visitor.visitVariables(self)
            else:
                return visitor.visitChildren(self)




    def variables(self):

        localctx = lenguajeutbParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variables)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(lenguajeutbParser.VARIABLES)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==lenguajeutbParser.TIPO:
                self.state = 46
                self.declaracion()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(lenguajeutbParser.FIN_VARIABLES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclaracionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPO(self):
            return self.getToken(lenguajeutbParser.TIPO, 0)

        def TIPO_VARIABLE(self):
            return self.getToken(lenguajeutbParser.TIPO_VARIABLE, 0)

        def NOMBRE(self):
            return self.getToken(lenguajeutbParser.NOMBRE, 0)

        def IDENTIFICADOR(self):
            return self.getToken(lenguajeutbParser.IDENTIFICADOR, 0)

        def VALOR_INICIAL(self):
            return self.getToken(lenguajeutbParser.VALOR_INICIAL, 0)

        def ENTERO(self):
            return self.getToken(lenguajeutbParser.ENTERO, 0)

        def REAL(self):
            return self.getToken(lenguajeutbParser.REAL, 0)

        def STRING(self):
            return self.getToken(lenguajeutbParser.STRING, 0)

        def BOOLEANO(self):
            return self.getToken(lenguajeutbParser.BOOLEANO, 0)

        def CHAR(self):
            return self.getToken(lenguajeutbParser.CHAR, 0)

        def getRuleIndex(self):
            return lenguajeutbParser.RULE_declaracion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = lenguajeutbParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaracion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(lenguajeutbParser.TIPO)
            self.state = 55
            self.match(lenguajeutbParser.TIPO_VARIABLE)
            self.state = 56
            self.match(lenguajeutbParser.NOMBRE)
            self.state = 57
            self.match(lenguajeutbParser.IDENTIFICADOR)
            self.state = 58
            self.match(lenguajeutbParser.VALOR_INICIAL)
            self.state = 59
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << lenguajeutbParser.ENTERO) | (1 << lenguajeutbParser.REAL) | (1 << lenguajeutbParser.STRING) | (1 << lenguajeutbParser.CHAR) | (1 << lenguajeutbParser.BOOLEANO))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SentenciasContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def imprimir(self):
            return self.getTypedRuleContext(lenguajeutbParser.ImprimirContext,0)


        def comentario(self):
            return self.getTypedRuleContext(lenguajeutbParser.ComentarioContext,0)


        def getRuleIndex(self):
            return lenguajeutbParser.RULE_sentencias

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencias" ):
                return visitor.visitSentencias(self)
            else:
                return visitor.visitChildren(self)




    def sentencias(self):

        localctx = lenguajeutbParser.SentenciasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_sentencias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [lenguajeutbParser.MOSTRAR]:
                self.state = 61
                self.imprimir()
                pass
            elif token in [lenguajeutbParser.NOTA]:
                self.state = 62
                self.comentario()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ImprimirContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOSTRAR(self):
            return self.getToken(lenguajeutbParser.MOSTRAR, 0)

        def IDENTIFICADOR(self):
            return self.getToken(lenguajeutbParser.IDENTIFICADOR, 0)

        def STRING(self):
            return self.getToken(lenguajeutbParser.STRING, 0)

        def getRuleIndex(self):
            return lenguajeutbParser.RULE_imprimir

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImprimir" ):
                return visitor.visitImprimir(self)
            else:
                return visitor.visitChildren(self)




    def imprimir(self):

        localctx = lenguajeutbParser.ImprimirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_imprimir)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(lenguajeutbParser.MOSTRAR)
            self.state = 66
            _la = self._input.LA(1)
            if not(_la==lenguajeutbParser.STRING or _la==lenguajeutbParser.IDENTIFICADOR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ComentarioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOTA(self):
            return self.getToken(lenguajeutbParser.NOTA, 0)

        def STRING(self):
            return self.getToken(lenguajeutbParser.STRING, 0)

        def getRuleIndex(self):
            return lenguajeutbParser.RULE_comentario

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComentario" ):
                return visitor.visitComentario(self)
            else:
                return visitor.visitChildren(self)




    def comentario(self):

        localctx = lenguajeutbParser.ComentarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comentario)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(lenguajeutbParser.NOTA)
            self.state = 69
            self.match(lenguajeutbParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





