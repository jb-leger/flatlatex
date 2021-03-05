# Copyright (c) 2016-2018, Jean-Benoist Leger <jb@leger.tf>
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


from .. import converter

def test_conv1():
    c = converter()
    r = c.convert(
        (
            r'\forall \eta>0\, \exists n\in\mathbb{N}\, \forall i>n\, '
            r'|u_i-\mathcal{l}|<\eta'
        )
    )
    assert r == '∀η>0 ∃n∈ℕ ∀i>n |uᵢ-𝓵|<η'


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

def test_conv5():
    c = converter()
    r = c.convert(r'\hat{p}')
    assert r == 'p\u0302'
    r = c.convert(r'p_1')
    assert r == 'p\u2081'
    r = c.convert(r'\hat{p}_1')
    assert r == 'p\u0302\u2081'
    r = c.convert(r'\hat{pc}_1')
    assert r == '(hat(pc))\u2081'


