
from .. import parser

def test_parser():
   
    expected = {
            r'\\': [('cmd', r'\\')],
            r'\cd': [('cmd', r'\cd')],
            r'ab': [('char','a'),('char','b')],
            r'e{to{t}o}e': [('char','e'),('subexpr','to{t}o'),('char','e')],
            r'g_f': [('char','g'),('oper','_'),('char','f')],
            r'h^i': [('char','h'),('oper','^'),('char','i')],
            }

    for k,v in expected.items():
        assert all([pki==vi for pki,vi in zip(parser.parse(k),v)]), "parser '%s'" % k

    for k1,v1 in expected.items():
        for k2,v2 in expected.items():
            assert all([pki==vi for pki,vi in zip(parser.parse(k1+' '+k2),v1+v2)]), "parser '%s'+'%s'" % (k1,k2)

