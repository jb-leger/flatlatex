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

"""
LaTeX math to Unicode text converter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

flatlatex is a basic converter from LaTeX math to human readable text math using
unicode characters.

Basic example:

    >>> import flatlatex
    >>> c = flatlatex.converter()
    >>> c.convert(
    ... r'\\forall \\eta>0\\, \\exists n\\in\\mathbb{N}\\, \\forall i>n\\, |u_i-\\mathcal{l}|<\\eta')
    '∀η>0 ∃n∊ℕ ∀i>n |uᵢ-𝓵|<η'

Commands can be added with LaTeX syntax:

    >>> import flatlatex
    >>> c = flatlatex.converter()
    >>> c.add_newcommand(r'\\newcommand\\prob{\\mathbb{P}}')
    >>> c.add_newcommand(r'\\newcommand\\binom[2]{\\frac{#2!}{#1!(#2-#1)!}}')
    >>> c.convert(r'\\prob(X=k)\\,=\\,\\binom{k}{n}\\times p^k(1-p)^{n-k}')
    'ℙ(X=k) = (n!)/(k!(n-k)!)×pᵏ(1-p)ⁿ⁻ᵏ'

The behavior can be change:

    >>> import flatlatex
    >>> c = flatlatex.converter()
    >>> c.convert(r'\\frac{8}{9}')
    '⁸⁄₉'
    >>> c.allow_zw = False
    >>> c.convert(r'\\frac{8}{9}')
    '8/9'
"""

__title__ = 'flatlatex'
__author__ = 'Jean-Benoist Leger'
__licence__ = 'BSD-2'

version_info = (0, 3)
__version__ = '.'.join(map(str, version_info))

from .conv import converter
