
from .. import data
from .. import parser

def test_known_fracts():
    assert type(data.known_fracts) is dict
    for k,v in data.known_fracts.items():
        assert type(k) is tuple
        assert len(k)==2
        assert all([type(x) is str for x in k])
        assert type(v) is str

def test_transliteration_consistancy():
    for d in (
            data.subscript,
            data.superscript,
            data.bb,
            data.bf,
            data.cal,
            data.frak,
            data.it,
            data.mono,
            ):
        assert type(d) is dict
        for k,v in d.items():
            assert type(k) is str
            assert type(v) is str

def test_symbols_consistancy():
    assert type(data.symbols) is dict
    for k,v in data.symbols.items():
        assert type(k) is str
        out=parser.parse(k)
        assert len(out)==1
        assert out[0][0] == 'cmd'
        assert type(v) is str

def test_combining_consistancy():
    assert type(data.combinings) is dict
    for k,v in data.combinings.items():
        assert type(k) is str
        out=parser.parse(k)
        assert len(out)==1
        assert out[0][0] == 'cmd'
        assert type(v) is tuple
        assert len(v) == 2
        assert all([type(x) is str for x in v])

def test_newcommands_consistancy():
    assert type(data.newcommands) is tuple
    for k in data.newcommands:
        parsed = parser.parse(k)
        assert len(parsed) in (3,6)
        assert parsed[0][0] == 'cmd'
        assert parsed[0][1] in (r'\newcommand', r'\renewcommand', r'\def')
        if len(parsed) == 6:
            assert parsed[2] == ('char','[')
            assert parsed[4] == ('char',']')
            assert type(parsed[3][0]) is str
            a = int(parsed[3][1])
            assert a>=0

def test_replicated_command():
    datasets = [
            data.symbols.keys(), 
            data.combinings.keys(),
            data.transliterators.keys(),
    ]
    datasets.append([parser.parse(nc)[1][1] for nc in data.newcommands])
    for i in range(len(datasets)):
        for j in range(i + 1, len(datasets)):
            s1 = set(datasets[i])
            s2 = set(datasets[j])
            assert len(s1.intersection(s2)) == 0

        

