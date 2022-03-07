from __future__ import annotations as __01asda1ha
from lark import Token as token
import dataclasses as dataclasses
import typing as typing
from .simplenote_require import (append,parseInt)

@dataclasses.dataclass
class Dashed:
    value: Note

@dataclasses.dataclass
class Dotted:
    value: Note

@dataclasses.dataclass
class Down7:
    value: Note

@dataclasses.dataclass
class Empty:
    pass

@dataclasses.dataclass
class Halfed:
    value: Note

@dataclasses.dataclass
class Raw:
    value: int

@dataclasses.dataclass
class Up7:
    value: Note

if typing.TYPE_CHECKING:
    Note = typing.Union[Up7,Raw,Halfed,Empty,Down7,Dotted,Dashed]
else:
    Note = (Up7,Raw,Halfed,Empty,Down7,Dotted,Dashed)

@dataclasses.dataclass
class Multi:
    value: list[Group]

@dataclasses.dataclass
class Single:
    value: Note

if typing.TYPE_CHECKING:
    Group = typing.Union[Single,Multi]
else:
    Group = (Single,Multi)

