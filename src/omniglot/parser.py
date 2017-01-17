from arpeggio import EOF
from arpeggio import OneOrMore
from arpeggio import Optional
from arpeggio import ParserPython
from arpeggio import RegExMatch as _
from arpeggio import ZeroOrMore


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


parser = ParserPython(calc, memoization=True)
parse_tree = parser.parse("-(4-1)*5+(2+4.67)+5.89/(.2+7)")
for i in parse_tree[0]:
    print(i)
