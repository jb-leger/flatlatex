# Copyright (c) 2016, Jean-Benoist Leger <jb@leger.tf>
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from . import data
from .transliteration import transliterator,transliterate
import regex
from . import latexfuntypes
from . import parser

class LatexSyntaxError(SyntaxError):
    pass

class converter:
    """flatlatex converter class

    :attrib allow_zw: boolean which indicate if zero width characters are allowed
        (True by default).
    :attrib allow_combinings: boolean which indicate if combining characters are allowed
        (True by default).
    """

    def __init__(self):
        """Initialize a convert method."""

        # transliteration
        self.__cmds = {
            r'\bb': transliterator(data.bb),
            r'\bf': transliterator(data.bf),
            r'\cal': transliterator(data.cal),
            r'\frak': transliterator(data.frak),
            r'\it': transliterator(data.it),
            r'\mono': transliterator(data.mono),
        }

        # symbols
        def makefun(symb):
            return lambda x: symb
        for cmd in data.symbols:
            self.__cmds[cmd] = latexfuntypes.latexfun(
                    makefun(data.symbols[cmd]),
                    0)

        # combinings
        def makefun(comb):
            return lambda x: self.__latexfun_comb(comb,x)
        for cmd in data.combinings:
            self.__cmds[cmd] = latexfuntypes.latexfun(
                    makefun(data.combinings[cmd]),
                    1)

        # others
        self.__cmds[r'\frac'] = latexfuntypes.latexfun(self.__latexfun_frac,2)
        self.__cmds[r'\sqrt'] = latexfuntypes.latexfun(self.__latexfun_sqrt,1)

        # newcommands
        for nc in data.newcommands:
            self.add_newcommand(nc)

        # config section
        self.allow_zw = True
        self.allow_combinings = True

    def convert(self, expr):
        """Convert LaTeX math to Unicode text.

        :param expr: LaTeX math expression to convert"""

        parsed = parser.parse(expr)
        outvec = []
        idx = 0
        while(idx < len(parsed)):
            element = parsed[idx]
            if element[0] == 'oper':
                outvec.append(('oper',element[1]))
                idx+=1
                continue
            if element[0] == 'char':
                outvec.append(('char',element[1]))
                idx+=1
                continue
            if element[0] == 'cmd':
                try:
                    pycmd = self.__cmds[element[1]]
                except KeyError:
                    outvec.append(('char',element[1]))
                    idx+=1
                    continue
                if len(parsed) <= idx+pycmd.nargs:
                    raise LatexSyntaxError
                args = [
                    self.convert(parsed[idx+k+1][1]) 
                    for k in range(pycmd.nargs)
                ]
                outvec.append(('char',pycmd.fun(args)))
                idx+=1+pycmd.nargs
                continue
            if element[0] == 'subexpr':
                outvec.append(('char',self.convert(element[1])))
                idx+=1
                continue
            raise Exception
        #subandsuperscript
        for idx in range(len(outvec)):
            if outvec[idx][0] == 'oper':
                if len(outvec) <= idx+1:
                    raise LatexSyntaxError
                if outvec[idx+1][0] == 'oper':
                    raise LatexSyntaxError
        for idx in range(len(outvec)):
            if outvec[idx][0] == 'oper' and outvec[idx][1] =='^':
                if idx+2 < len(outvec):
                    if outvec[idx+2][0] == 'oper' and outvec[idx+2][1]=='_':
                        # we invert ^ and _
                        (
                            outvec[idx],
                            outvec[idx+1],
                            outvec[idx+2],
                            outvec[idx+3],
                        ) = (
                            outvec[idx+2],
                            outvec[idx+3],
                            outvec[idx],
                            outvec[idx+1],
                        )
        # sub
        newoutvec = []
        idx = 0
        while idx<len(outvec):
            if idx+1<len(outvec):
                if outvec[idx+1][0] == 'oper' and outvec[idx+1][1] == '_':
                    newoutvec.append(
                        (
                            'char',
                            self.__indexed(
                                outvec[idx][1],
                                outvec[idx+2][1]
                            ),
                        )
                    )
                    idx+=3
                    continue
            newoutvec.append(outvec[idx])
            idx+=1
        outvec = newoutvec
        # super
        newoutvec = []
        idx = 0
        while idx<len(outvec):
            if idx+1<len(outvec):
                if outvec[idx+1][0] == 'oper' and outvec[idx+1][1] == '^':
                    newoutvec.append(
                        (
                            'char',
                            self.__exponent(
                                outvec[idx][1],
                                outvec[idx+2][1]
                            ),
                        )
                    )
                    idx+=3
                    continue
            newoutvec.append(outvec[idx])
            idx+=1
        outvec = newoutvec
        return ''.join([x[1] for x in outvec])

    def __indexed(self,a,b):
        f_sub = transliterate(data.subscript)
        bsub,ok = f_sub(b)
        if self.__is_complex_expr(a):
            a = '('+a+')'
        if ok:
            return a+bsub
        return a+'['+b+']'
    
    def __exponent(self,a,b):
        f_sup = transliterate(data.superscript)
        bsup,ok = f_sup(b)
        if self.__is_complex_expr(a):
            a = '('+a+')'
        if ok:
            return a+bsup
        if self.__is_complex_expr(b):
            b = '('+b+')'
        return a+'^'+b

    def __is_complex_expr(self, expr):
        return (len(expr)>1)

    def __latexfun_comb(self, comb, inputs):
        expr = inputs[0]
        if(len(expr)==1):
            if self.allow_combinings:
                return expr + comb[0]
        return comb[1] + '(' + expr + ')'

    def add_newcommand(self, one_newcommand):
        """Add a command definiton using LaTeX syntax.

        :param expr: a valid \\newcommand (or \\renewcommand or \\def)
            definition.
            Examples:
            - r'\\newcommand\\prob{\\mathbb{P}}'
            - r'\\newcommand\\binom[2]{\\frac{#2!}{#1!(#2-#1)!}}'
        """

        parsed = parser.parse(one_newcommand)
        if not (len(parsed) in (3,6)):
            raise LatexSyntaxError
        ok=False
        if parsed[0][0] == 'cmd':
            if parsed[0][1] in (
                    r'\newcommand',
                    r'\renewcommand',
                    r'\def'):
                ok=True
        if not ok:
            raise LatexSyntaxError
        nargs = 0
        if len(parsed)==6:
            if parsed[2] == ('char','[') and parsed[4] == ('char',']'):
                nargs = int(parsed[3][1])
            else:
                raise LatexSyntaxError
        cmdname = parsed[1][1]
        cmdexpr = parsed[-1][1]

        def thefun(args):
            expr = cmdexpr
            for i in range(len(args)):
                expr = regex.sub('#%i'%(i+1),args[i],expr)
            return self.convert(expr)

        self.__cmds[cmdname] = latexfuntypes.latexfun(
                lambda x: thefun(x),
                nargs)
        return None

    def __latexfun_frac(self,inputs):
        a = inputs[0]
        b = inputs[1]

        try:
            ret = data.known_fracts[(a,b)]
            return ret
        except KeyError:
            pass
        
        if self.allow_zw:
            f_sub = transliterate(data.subscript)
            f_sup = transliterate(data.superscript)

            a_sup,ok_sup = f_sup(a)
            b_sub,ok_sub = f_sub(b)

            if ok_sup and ok_sub:
                return a_sup+'⁄'+b_sub
        
        if self.__is_complex_expr(a):
            a = '('+a+')'
        if self.__is_complex_expr(b):
            b = '('+b+')'
        return a+'/'+b

    def __latexfun_sqrt(self,inputs):
        a = inputs[0]

        if self.__is_complex_expr(a):
            a = '(' + a + ')'
        return '√'+a


    

