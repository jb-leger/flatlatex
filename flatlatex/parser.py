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

import regex

def parse_one_element(s):
    R = r'((?>\\(?:[^A-Za-z]|[A-Za-z]+))|(?>[^\{\}\\])|\{(?1)*\})'
    r = regex.match(R,s)
    s = s[r.span()[1]:]
    c = r.captures()[0]
    if c[0] == '\\':
        return ( ('cmd', c), s)
    if c[0] == '{':
        return ( ('subexpr', c[1:-1]), s)
    if c in ('_','^'):
        return ( ('oper', c), s)
    return ( ('char', c), s)

def parse(s):
    l = []
    while len(s)>0:
        m,s = parse_one_element(s)
        if not (m[1] == ' '):
            l.append(m)
    return l
