from _tbnf.FableSedlex.sedlex import *
import typing
import typing_extensions
import dataclasses
_sedlex_rnd_13 = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -1 ]  # token_ids

def _sedlex_st_0(lexerbuf: lexbuf):
    result = -1
    state_id = _sedlex_decide_1(public_next_int(lexerbuf))
    if state_id >= 0:
        result = _sedlex_rnd_12[state_id](lexerbuf)
    else:
        result = backtrack(lexerbuf)
    return result

def _sedlex_decide_1(c: int):
    if c <= 95:
        return _sedlex_DT_table_1[c - -1] - 1
    else:
        return 1

def _sedlex_rnd_11(lexerbuf: lexbuf):
    result = -1
    result = 7
    return result

def _sedlex_rnd_10(lexerbuf: lexbuf):
    result = -1
    result = 6
    return result

def _sedlex_rnd_9(lexerbuf: lexbuf):
    result = -1
    result = 5
    return result

def _sedlex_rnd_8(lexerbuf: lexbuf):
    result = -1
    result = 8
    return result

def _sedlex_rnd_7(lexerbuf: lexbuf):
    result = -1
    result = 4
    return result

def _sedlex_rnd_6(lexerbuf: lexbuf):
    result = -1
    result = 3
    return result

def _sedlex_rnd_5(lexerbuf: lexbuf):
    result = -1
    result = 2
    return result

def _sedlex_rnd_4(lexerbuf: lexbuf):
    result = -1
    result = 1
    return result

def _sedlex_rnd_3(lexerbuf: lexbuf):
    result = -1
    result = 0
    return result

def _sedlex_rnd_2(lexerbuf: lexbuf):
    result = -1
    result = 9
    return result

def _sedlex_rnd_1(lexerbuf: lexbuf):
    result = -1
    result = 10
    return result


@dataclasses.dataclass
class Token:
    token_id: int
    lexeme : str
    line: int
    col: int
    span: int
    offset: int
    file: str

_Token = typing.TypeVar("_Token")

class TokenConstructor(typing_extensions.Protocol[_Token]):
    def __call__(self, token_id: int, lexeme: str, line: int, col: int, span: int, offset: int, file: str) -> _Token: ...

def lex(lexerbuf: lexbuf ,  construct_token: TokenConstructor[_Token]=Token):
    start(lexerbuf)
    case_id = _sedlex_st_0(lexerbuf)
    if case_id < 0: raise Exception("the last branch must be a catch-all error case!")
    token_id = _sedlex_rnd_13[case_id]
    if token_id is not None:
        return construct_token(token_id, lexeme(lexerbuf), lexerbuf.start_line, lexerbuf.pos - lexerbuf.curr_bol, lexerbuf.pos - lexerbuf.start_pos, lexerbuf.start_pos, lexerbuf.filename)
    return None
def lexall(buf: lexbuf, construct: TokenConstructor[_Token], is_eof: Callable[[_Token], bool]):
    while True:
        token = lex(buf, construct)
        if token is None: continue
        if is_eof(token): break
        yield token
_sedlex_DT_table_1 = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 2, 2, 2, 5, 6, 2, 7, 8, 8, 8, 8, 8, 8, 8, 2, 2, 2, 2, 9, 2, 10, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 11]

_sedlex_rnd_12 = [_sedlex_rnd_1, _sedlex_rnd_2, _sedlex_rnd_3, _sedlex_rnd_4, _sedlex_rnd_5, _sedlex_rnd_6, _sedlex_rnd_7, _sedlex_rnd_8, _sedlex_rnd_9, _sedlex_rnd_10, _sedlex_rnd_11]

