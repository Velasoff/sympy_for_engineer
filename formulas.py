from sympy import *
import re


class f:
    def __init__(self, exp: str):
        self.sym_pattern = re.compile('\([a-z]\)|\s[a-z]\)|\s[a-z]\s|\([a-z]\s|^[a-z]\s|\s[a-z]$')
        self.sym_detect(exp)
        globals().update({sym.name: sym for sym in symbols(self.list_sym)})
        self.exp = eval(exp)
        # self.eq = Eq(self.exp, self.exp.doit())
        init_printing(use_unicode=True)

    def __repr__(self):
        return str(self.exp)

    def sym_detect(self, exp):
        try:
            list_sym = re.findall(self.sym_pattern, exp)
            self.list_sym = set([re.sub('\(|\)|\s', '', sym) for sym in list_sym])
        except Exception as e:
            self.list_sym = set()
