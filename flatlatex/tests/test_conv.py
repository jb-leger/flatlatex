from .. import converter


def test_conv1():
    c = converter()
    r = c.convert(
            r'\forall \eta>0\, \exists n\in\mathbb{N}\, \forall i>n\, |u_i-\mathcal{l}|<\eta')
    assert r=='∀η>0 ∃n∊ℕ ∀i>n |uᵢ-𝓵|<η'

def test_conv2():
    c = converter()
    c.add_newcommand(r'\newcommand\prob{\mathbb{P}}')
    c.add_newcommand(r'\newcommand\binom[2]{\frac{#2!}{#1!(#2-#1)!}}')
    r = c.convert(r'\prob(X=k)\,=\,\binom{k}{n}\times p^k(1-p)^{n-k}')
    assert r == 'ℙ(X=k) = (n!)/(k!(n-k)!)×pᵏ(1-p)ⁿ⁻ᵏ'

def test_conv3():
    c = converter()
    c.allow_zw = True
    r = c.convert(r'\frac{8}{9}')
    assert r == '⁸⁄₉'
    c.allow_zw = False
    r = c.convert(r'\frac{8}{9}')
    assert r == '8/9'

def test_conv4():
    c = converter()
    c.allow_combinings = True
    r = c.convert(r'\hat\alpha')
    assert r == '\u03B1\u0302'
    c.allow_combinings = False
    r = c.convert(r'\hat\alpha')
    assert r == 'hat(\u03B1)'
