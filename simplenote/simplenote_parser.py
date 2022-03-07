from __future__ import annotations
from .simplenote_require import (append,parseInt)
from .simplenote_lexer import lexall as lexall
from .simplenote_construct import *
from lark.lexer import Lexer as Lexer
from lark import Transformer as Transformer
from lark import Lark as Lark
from _tbnf.FableSedlex.sedlex import from_ustring as from_ustring
tokenmaps = ["_I__O__I_", "_I__P__I_", "_I__T__I_", "_I__U__I_", "_I_0_I_", "_I__I__I_", "_I__K__I_", "_I___I_", "NOTE", "UNKNOWN"]
tokenreprs = ["\"(\"", "\")\"", "\"-\"", "\".\"", "\"0\"", "\"<\"", "\">\"", "\"_\"", "NOTE", "UNKNOWN"]

def construct_token(token_id, lexeme, line, col, span, offset, file):
    if token_id == -1: return token("EOF", "")
    return token(tokenmaps[token_id], lexeme, offset, line, col, None, None, span + offset)

def is_eof(token):
    return token.type == "EOF"
class Sedlex(Lexer):
    def __init__(self, lex_conf):
        pass
    def lex(self, raw_string):
        lexbuf = from_ustring(raw_string)
        return lexall(lexbuf, construct_token, is_eof)

class RBNFTransformer(Transformer):
    def start_0(self, __tbnf_COMPONENTS):
        return __tbnf_COMPONENTS[0]
    
    def tops_1(self, __tbnf_COMPONENTS):
        return append(__tbnf_COMPONENTS[0], __tbnf_COMPONENTS[1])
    
    def tops_0(self, __tbnf_COMPONENTS):
        return [__tbnf_COMPONENTS[0]]
    
    def top_1(self, __tbnf_COMPONENTS):
        return Multi(__tbnf_COMPONENTS[1])
    
    def top_0(self, __tbnf_COMPONENTS):
        return Multi([Single(__tbnf_COMPONENTS[0])])
    
    def elements_1(self, __tbnf_COMPONENTS):
        return append(__tbnf_COMPONENTS[0], __tbnf_COMPONENTS[1])
    
    def elements_0(self, __tbnf_COMPONENTS):
        return [__tbnf_COMPONENTS[0]]
    
    def group_1(self, __tbnf_COMPONENTS):
        return Single(__tbnf_COMPONENTS[0])
    
    def group_0(self, __tbnf_COMPONENTS):
        return Multi(__tbnf_COMPONENTS[1])
    
    def note_6(self, __tbnf_COMPONENTS):
        return Empty()
    
    def note_5(self, __tbnf_COMPONENTS):
        return Halfed(__tbnf_COMPONENTS[0])
    
    def note_4(self, __tbnf_COMPONENTS):
        return Dashed(__tbnf_COMPONENTS[0])
    
    def note_3(self, __tbnf_COMPONENTS):
        return Dotted(__tbnf_COMPONENTS[0])
    
    def note_2(self, __tbnf_COMPONENTS):
        return Down7(__tbnf_COMPONENTS[0])
    
    def note_1(self, __tbnf_COMPONENTS):
        return Up7(__tbnf_COMPONENTS[0])
    
    def note_0(self, __tbnf_COMPONENTS):
        return Raw(parseInt(__tbnf_COMPONENTS[0]))
    
    pass

with (__import__('pathlib').Path(__file__).parent /'simplenote.lark').open(encoding='utf8') as __0123fx9:
    grammar = __0123fx9.read()

parser = Lark(grammar, start='start', parser='lalr', lexer=Sedlex, transformer=RBNFTransformer(), keep_all_tokens=True)
