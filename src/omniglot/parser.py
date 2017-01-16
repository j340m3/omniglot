from arpeggio import Optional, ZeroOrMore, OneOrMore, EOF
from arpeggio import RegExMatch as _
from arpeggio import ParserPython


def number():
    return _(r'\d*\.\d*|\d+')


def factor():
    return Optional(["+", "-"]), [number, ("(", expression, ")")]


def term():
    return factor, ZeroOrMore(["*", "/"], factor)


def expression():
    return term, ZeroOrMore(["+", "-"], term)


def calc():
    return OneOrMore(expression), EOF

parser = ParserPython(calc)

