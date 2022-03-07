import pynput.keyboard as pynput

C = pynput.Controller()
import time

time.sleep(2)


def note(c, t):
    if c != ' ':
        C.press(c)
    try:
        time.sleep(t)
    finally:
        if c != ' ':
            C.release(c)

def notes(cs, t):
    for c in cs:
        note(c, t)

def play(t):
    notes('gg dfdfg d gh gfdfg ', t)
    notes('gk jhgfd fg ds dfdsd ', t)
    notes('gk jhgfd fg ds dfdsa a', t)



"(1>.)(7__7_)(1>1>-)"
"(1>.)(7__7_)(1>1>)(01_)"
"(1>.)(7__7_)(6_(6)5_)(5_5-)"
"(0_)(3_3_)(5_)(5_(6_6))(0_)(6_6_)(1>_)"
"(2>_.(3>__3>))(0_.)(1>__1>_)(2>_)(2>(3>--3>---))"

