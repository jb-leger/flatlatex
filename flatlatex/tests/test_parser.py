# Copyright (c) 2017-2018, Jean-Benoist Leger <jb@leger.tf>
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


from .. import parser


def test_parser():

    expected = {
            r'\\': [('cmd',  r'\\')],
            r'\cd': [('cmd',  r'\cd')],
            r'ab': [('char', 'a'), ('char', 'b')],
            r'e{to{t}o}e': [
                ('char', 'e'), ('subexpr', 'to{t}o'), ('char', 'e')
            ],
            r'g_f': [('char', 'g'), ('oper', '_'), ('char', 'f')],
            r'h^i': [('char', 'h'), ('oper', '^'), ('char', 'i')],
            }

    for k, v in expected.items():
        assert all([
            pki == vi
            for pki, vi in zip(parser.parse(k), v)
        ]), "parser '%s'" % k

    for k1, v1 in expected.items():
        for k2, v2 in expected.items():
            assert all([
                pki == vi
                for pki, vi in zip(parser.parse(k1 + ' ' + k2), v1 + v2)
            ]), "parser '%s'+'%s'" % (k1, k2)
