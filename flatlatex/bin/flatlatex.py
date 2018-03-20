#!/usr/bin/env python3
#
# Copyright (c) 2018, Pierre-Elliott Bécue
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
This is a rough binary command that casts a converter and calls
convert on the user's input.
"""

import argparse

import flatlatex


def do_convert(arguments):
    """Do the actual conversion"""

    converter = flatlatex.converter(
        arguments.disallow_zero_width,
        arguments.disallow_combinings,
    )

    return converter.convert(arguments.input[0])


def main():
    parser = argparse.ArgumentParser(
        description="Convert latex entries to flat unicode"
    )
    parser.add_argument('-C', '--disallow-combinings',
                        help="Disallow combining characters to be used",
                        action="store_false",
                        default=True)
    parser.add_argument('-Z', '--disallow-zero-width',
                        help="Disallow zero-width characters to be used",
                        action="store_false",
                        default=True)
    parser.add_argument("input", type=str, nargs=1,
                        help="The latex string to convert")

    args = parser.parse_args()

    ret = do_convert(args)
    print(ret)
