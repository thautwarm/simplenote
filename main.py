from collections import defaultdict
import time
from typing import DefaultDict
from simplenote.simplenote_parser import parser
from simplenote.simplenote_construct import *
from contextlib import contextmanager
import pynput.keyboard as pynput
C = pynput.Controller()

# https://www.bilibili.com/read/cv3745169
notes = (
    "1>.(7__7_)(1>1>-)"
    "1>.(7__7_)(1>1>)(01_)"
    "1>.(7__7_)(6_(6)5_)(5_5-)"
    "0_(3_3_)5_(5_(6_6))0_(6_6_)1>_"
    "(2>_.(3>__3>))0_.(1>__1>_)2>_(2>(3>--3>---))"
    "0000"
    "6_.(1>__1>_)(7_7_)5_6_.(5__5-)2_1__1__2_3__(3__3_)(6<_6<-)0"
    "0_5<_2__2_(3__3_)2_3_5_"
    "6_.(1>__1>_)(7_7_)5_6_.(5_"
    "_5)0_5__5__3>__2>__3>__2>__3>_4>__(3>__"
    "3>_)(1>_1>-)0_1>_"
    "7_.(7__7_)1>_2>0_1>_"
    "2>_.(1>__1>_)(6_6_)1>_3>_.(2>__2>-)00_1>_"
    "2>_.(1>__1>_)(6_6_)1>_(5>5>-)00_1>_"
    "2>_.(1>__1>_)(6_6_)1>_3>_(2>_"
    "2>)2>_3>_2>_3>_(5>_3>_)2>_.(1>__1>-)0_1>_"
    "7_.(6__7_)1>_2>-"
    "1>_.(7__7_)(1>_1>-)"
    "1>_.(7__7_)(1>_1>)0_1_"
    "1>_.(7__7_)(6_65_)(5_"
    "5-)0_(3_3_)5_"
    "(5_.(6__6_))0_(6_6_)1>_"
    "(1>_.2>__2>)0_.(1>__1>_)2>(2>3>--)"
    "05_.5__53>"
    "2>_3>_5>_3>_2>_3>__(3>__3_>)1>_"
    "2>_3>_5>_3>_2>_3>__(3>__3>_)5_"
    "5_1>__(1>__1>_)5_5_1>_2>_1>_"
    "5>4>3>_.(2>__2>_)1>_"
    "(1>1>_)(1>_1_>)2>_3>_(2>_"
    "2>)5_(2>_2>_)3>_5>_(2>_"
    "3>--)0"
    "0553>"
    "2>_3>_5>_3>_2>_3>__(3>__3>_)1>__1>__"
    "2>_3>_5>_3>_2>_3>__(1>__1>_)1>_"
    "1>_.(2>__2>_)(3>_3>_)3>_1>>_(7>_"
    "7>)5>3>_.(2>__2>_)1>_"
    "(1>1>_)(1>_1>_)2>_3>_(2>_"
    "2>)0_5_5_5_(6"
    "6--)0"
    "0000"
)

def compile(x: Note) -> tuple[int | None, float]:
    if isinstance(x, Raw):
        return x.value, 0.25
    if isinstance(x, Up7):
        a, t = compile(x.value)
        if isinstance(a, int) :
            a = a + 7
        return a, t
    if isinstance(x, Down7):
        a, t = compile(x.value)
        if isinstance(a, int) :
            a = a - 7
        return a, t
    if isinstance(x, Dotted):
        a, t = compile(x.value)
        return a, t * 1.5
    if isinstance(x, Dashed):
        a, t = compile(x.value)
        return a, t + 0.25
    if isinstance(x, Halfed):
        a, t = compile(x.value)
        return a, t * 0.5
    if isinstance(x, Empty):
        return None, 0.25
    raise TypeError("invalid note " + x.__class__.__name__)


def press(x: int | None):
    print("press", x)
    if x is not None:
        with up_or_down((x - 1) // 7):
            return C.press(to_note(x))

def release(x: int | None):
    print("release", x)
    if x is not None:
        with up_or_down((x - 1) // 7):
            return C.release(to_note(x))


global_states: DefaultDict[int | None, float] = defaultdict(float)
available_notes = 'asdfghj'

def pressed(key):
    C.press(key)
    time.sleep(0.01)
    C.release(key)

@contextmanager
def up_or_down(n):
    if n < 0:
        for i in range(-n):
            pressed('z')
            time.sleep(0.01)
    else:
        for i in range(n):
            pressed('x')
            time.sleep(0.01)
    try:
        yield
    finally:
        if n < 0:
            for i in range(-n):
                pressed('x')
                time.sleep(0.01)
        else:
            for i in range(n):
                pressed('z')
                time.sleep(0.01)

def to_note(i: int):
    return available_notes[(i - 1) % 7]


def clean(g: dict[int | None, float], pressed: DefaultDict[int | None, bool]):
    g_st = list(g.items())
    for k, v in g_st:
        if v == 0.0:
            if pressed[k]:
                release(k)
                pressed[k] = False

def unpress(g: dict[int | None, float], t: float):
    g_st = list(g.items())
    for k, v in g_st:
        g[k] = max(v - t, 0.0)

def interpret(g: dict[int | None, float], pressed: DefaultDict[int | None, bool], x):
    if isinstance(x, Single):
        a, t = compile(x.value)
        if g[a] == 0.0:
            if pressed[a]:
                pass
            else:
                press(a)
                pressed[a] = True
        g[a] += t
        clean(g, pressed)
        unpress(g, t)
        time.sleep(t)
        return
    if isinstance(x, Multi):
        local_pressed = defaultdict(bool)
        for each in x.value:
            interpret(g, local_pressed, each)
        for each, is_pressed in local_pressed.items():
            if is_pressed:
                g[each] = 0.0
                release(each)
        return

seqs = parser.parse(notes)
time.sleep(5)
local_pressed = defaultdict(bool)
global_state = defaultdict(float)
for each in seqs:
    interpret(global_state, local_pressed, each)

_, t = max(global_state.items(), key=lambda x: x[1])
unpress(global_state, t + 0.1)
clean(global_state, local_pressed)
