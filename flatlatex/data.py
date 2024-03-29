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

known_fracts = {
    ("1", "2"): "½",
    ("1", "3"): "⅓",
    ("2", "3"): "⅔",
    ("1", "4"): "¼",
    ("3", "4"): "¾",
    ("1", "5"): "⅕",
    ("2", "5"): "⅖",
    ("3", "5"): "⅗",
    ("4", "5"): "⅘",
    ("1", "6"): "⅙",
    ("5", "6"): "⅚",
    ("1", "7"): "⅐",
    ("1", "8"): "⅛",
    ("3", "8"): "⅜",
    ("5", "8"): "⅝",
    ("7", "8"): "⅞",
    ("1", "9"): "⅑",
}

subscript = {
    "0": "₀",
    "1": "₁",
    "2": "₂",
    "3": "₃",
    "4": "₄",
    "5": "₅",
    "6": "₆",
    "7": "₇",
    "8": "₈",
    "9": "₉",
    "+": "₊",
    "-": "₋",
    "=": "₌",
    "(": "₍",
    ")": "₎",
    "a": "ₐ",
    "e": "ₑ",
    "i": "ᵢ",
    "j": "\N{LATIN SUBSCRIPT SMALL LETTER J}",
    "o": "ₒ",
    "r": "ᵣ",
    "u": "ᵤ",
    "v": "ᵥ",
    "x": "ₓ",
    "β": "ᵦ",
    "γ": "ᵧ",
    "ρ": "ᵨ",
    "φ": "ᵩ",
    "χ": "ᵪ",
}

superscript = {
    "0": "⁰",
    "1": "¹",
    "2": "²",
    "3": "³",
    "4": "⁴",
    "5": "⁵",
    "6": "⁶",
    "7": "⁷",
    "8": "⁸",
    "9": "⁹",
    "+": "⁺",
    "-": "⁻",
    "=": "⁼",
    "(": "⁽",
    ")": "⁾",
    "a": "ᵃ",
    "b": "ᵇ",
    "c": "ᶜ",
    "d": "ᵈ",
    "e": "ᵉ",
    "f": "ᶠ",
    "g": "ᵍ",
    "h": "ʰ",
    "i": "ⁱ",
    "j": "ʲ",
    "k": "ᵏ",
    "l": "ˡ",
    "m": "ᵐ",
    "n": "ⁿ",
    "o": "ᵒ",
    "p": "ᵖ",
    "r": "ʳ",
    "s": "ˢ",
    "t": "ᵗ",
    "u": "ᵘ",
    "v": "ᵛ",
    "w": "ʷ",
    "x": "ˣ",
    "y": "ʸ",
    "z": "ᶻ",
    "A": "ᴬ",
    "B": "ᴮ",
    "D": "ᴰ",
    "E": "ᴱ",
    "G": "ᴳ",
    "H": "ᴴ",
    "I": "ᴵ",
    "J": "ᴶ",
    "K": "ᴷ",
    "L": "ᴸ",
    "M": "ᴹ",
    "N": "ᴺ",
    "O": "ᴼ",
    "P": "ᴾ",
    "R": "ᴿ",
    "T": "ᵀ",
    "U": "ᵁ",
    "V": "ⱽ",
    "W": "ᵂ",
    "α": "ᵅ",
    "β": "ᵝ",
    "γ": "ᵞ",
    "δ": "ᵟ",
    "∊": "ᵋ",
    "θ": "ᶿ",
    "ι": "ᶥ",
    "Φ": "ᶲ",
    "φ": "ᵠ",
    "χ": "ᵡ",
}

bb = {
    "A": "𝔸",
    "B": "𝔹",
    "C": "ℂ",
    "D": "𝔻",
    "E": "𝔼",
    "F": "𝔽",
    "G": "𝔾",
    "H": "ℍ",
    "I": "𝕀",
    "J": "𝕁",
    "K": "𝕂",
    "L": "𝕃",
    "M": "𝕄",
    "N": "ℕ",
    "O": "𝕆",
    "P": "ℙ",
    "Q": "ℚ",
    "R": "ℝ",
    "S": "𝕊",
    "T": "𝕋",
    "U": "𝕌",
    "V": "𝕍",
    "W": "𝕎",
    "X": "𝕏",
    "Y": "𝕐",
    "Z": "ℤ",
    "a": "𝕒",
    "b": "𝕓",
    "c": "𝕔",
    "d": "𝕕",
    "e": "𝕖",
    "f": "𝕗",
    "g": "𝕘",
    "h": "𝕙",
    "i": "𝕚",
    "j": "𝕛",
    "k": "𝕜",
    "l": "𝕝",
    "m": "𝕞",
    "n": "𝕟",
    "o": "𝕠",
    "p": "𝕡",
    "q": "𝕢",
    "r": "𝕣",
    "s": "𝕤",
    "t": "𝕥",
    "u": "𝕦",
    "v": "𝕧",
    "w": "𝕨",
    "x": "𝕩",
    "y": "𝕪",
    "z": "𝕫",
    "0": "𝟘",
    "1": "𝟙",
    "2": "𝟚",
    "3": "𝟛",
    "4": "𝟜",
    "5": "𝟝",
    "6": "𝟞",
    "7": "𝟟",
    "8": "𝟠",
    "9": "𝟡",
}

bf = {
    "A": "𝐀",
    "B": "𝐁",
    "C": "𝐂",
    "D": "𝐃",
    "E": "𝐄",
    "F": "𝐅",
    "G": "𝐆",
    "H": "𝐇",
    "I": "𝐈",
    "J": "𝐉",
    "K": "𝐊",
    "L": "𝐋",
    "M": "𝐌",
    "N": "𝐍",
    "O": "𝐎",
    "P": "𝐏",
    "Q": "𝐐",
    "R": "𝐑",
    "S": "𝐒",
    "T": "𝐓",
    "U": "𝐔",
    "V": "𝐕",
    "W": "𝐖",
    "X": "𝐗",
    "Y": "𝐘",
    "Z": "𝐙",
    "a": "𝐚",
    "b": "𝐛",
    "c": "𝐜",
    "d": "𝐝",
    "e": "𝐞",
    "f": "𝐟",
    "g": "𝐠",
    "h": "𝐡",
    "i": "𝐢",
    "j": "𝐣",
    "k": "𝐤",
    "l": "𝐥",
    "m": "𝐦",
    "n": "𝐧",
    "o": "𝐨",
    "p": "𝐩",
    "q": "𝐪",
    "r": "𝐫",
    "s": "𝐬",
    "t": "𝐭",
    "u": "𝐮",
    "v": "𝐯",
    "w": "𝐰",
    "x": "𝐱",
    "y": "𝐲",
    "z": "𝐳",
    "Α": "𝚨",
    "Β": "𝚩",
    "Γ": "𝚪",
    "Δ": "𝚫",
    "Ε": "𝚬",
    "Ζ": "𝚭",
    "Η": "𝚮",
    "Θ": "𝚯",
    "Ι": "𝚰",
    "Κ": "𝚱",
    "Λ": "𝚲",
    "Μ": "𝚳",
    "Ν": "𝚴",
    "Ξ": "𝚵",
    "Ο": "𝚶",
    "Π": "𝚷",
    "Ρ": "𝚸",
    "ϴ": "𝚹",
    "Σ": "𝚺",
    "Τ": "𝚻",
    "Υ": "𝚼",
    "Φ": "𝚽",
    "Χ": "𝚾",
    "Ψ": "𝚿",
    "Ω": "𝛀",
    "∇": "𝛁",
    "α": "𝛂",
    "β": "𝛃",
    "γ": "𝛄",
    "δ": "𝛅",
    "ε": "𝛆",
    "ζ": "𝛇",
    "η": "𝛈",
    "θ": "𝛉",
    "ι": "𝛊",
    "κ": "𝛋",
    "λ": "𝛌",
    "μ": "𝛍",
    "ν": "𝛎",
    "ξ": "𝛏",
    "ο": "𝛐",
    "π": "𝛑",
    "ρ": "𝛒",
    "ς": "𝛓",
    "σ": "𝛔",
    "τ": "𝛕",
    "υ": "𝛖",
    "φ": "𝛗",
    "χ": "𝛘",
    "ψ": "𝛙",
    "ω": "𝛚",
    "∂": "𝛛",
    "ϵ": "𝛜",
    "ϑ": "𝛝",
    "ϰ": "𝛞",
    "ϕ": "𝛟",
    "ϱ": "𝛠",
    "ϖ": "𝛡",
    "0": "𝟎",
    "1": "𝟏",
    "2": "𝟐",
    "3": "𝟑",
    "4": "𝟒",
    "5": "𝟓",
    "6": "𝟔",
    "7": "𝟕",
    "8": "𝟖",
    "9": "𝟗",
}

cal = {
    "A": "𝓐",
    "B": "𝓑",
    "C": "𝓒",
    "D": "𝓓",
    "E": "𝓔",
    "F": "𝓕",
    "G": "𝓖",
    "H": "𝓗",
    "I": "𝓘",
    "J": "𝓙",
    "K": "𝓚",
    "L": "𝓛",
    "M": "𝓜",
    "N": "𝓝",
    "O": "𝓞",
    "P": "𝓟",
    "Q": "𝓠",
    "R": "𝓡",
    "S": "𝓢",
    "T": "𝓣",
    "U": "𝓤",
    "V": "𝓥",
    "W": "𝓦",
    "X": "𝓧",
    "Y": "𝓨",
    "Z": "𝓩",
    "a": "𝓪",
    "b": "𝓫",
    "c": "𝓬",
    "d": "𝓭",
    "e": "𝓮",
    "f": "𝓯",
    "g": "𝓰",
    "h": "𝓱",
    "i": "𝓲",
    "j": "𝓳",
    "k": "𝓴",
    "l": "𝓵",
    "m": "𝓶",
    "n": "𝓷",
    "o": "𝓸",
    "p": "𝓹",
    "q": "𝓺",
    "r": "𝓻",
    "s": "𝓼",
    "t": "𝓽",
    "u": "𝓾",
    "v": "𝓿",
    "w": "𝔀",
    "x": "𝔁",
    "y": "𝔂",
    "z": "𝔃",
}

frak = {
    "A": "𝔄",
    "B": "𝔅",
    "C": "ℭ",
    "D": "𝔇",
    "E": "𝔈",
    "F": "𝔉",
    "G": "𝔊",
    "H": "ℌ",
    "I": "ℑ",
    "J": "𝔍",
    "K": "𝔎",
    "L": "𝔏",
    "M": "𝔐",
    "N": "𝔑",
    "O": "𝔒",
    "P": "𝔓",
    "Q": "𝔔",
    "R": "ℜ",
    "S": "𝔖",
    "T": "𝔗",
    "U": "𝔘",
    "V": "𝔙",
    "W": "𝔚",
    "X": "𝔛",
    "Y": "𝔜",
    "Z": "ℨ",
    "a": "𝔞",
    "b": "𝔟",
    "c": "𝔠",
    "d": "𝔡",
    "e": "𝔢",
    "f": "𝔣",
    "g": "𝔤",
    "h": "𝔥",
    "i": "𝔦",
    "j": "𝔧",
    "k": "𝔨",
    "l": "𝔩",
    "m": "𝔪",
    "n": "𝔫",
    "o": "𝔬",
    "p": "𝔭",
    "q": "𝔮",
    "r": "𝔯",
    "s": "𝔰",
    "t": "𝔱",
    "u": "𝔲",
    "v": "𝔳",
    "w": "𝔴",
    "x": "𝔵",
    "y": "𝔶",
    "z": "𝔷",
}

it = {
    "A": "𝐴",
    "B": "𝐵",
    "C": "𝐶",
    "D": "𝐷",
    "E": "𝐸",
    "F": "𝐹",
    "G": "𝐺",
    "H": "𝐻",
    "I": "𝐼",
    "J": "𝐽",
    "K": "𝐾",
    "L": "𝐿",
    "M": "𝑀",
    "N": "𝑁",
    "O": "𝑂",
    "P": "𝑃",
    "Q": "𝑄",
    "R": "𝑅",
    "S": "𝑆",
    "T": "𝑇",
    "U": "𝑈",
    "V": "𝑉",
    "W": "𝑊",
    "X": "𝑋",
    "Y": "𝑌",
    "Z": "𝑍",
    "a": "𝑎",
    "b": "𝑏",
    "c": "𝑐",
    "d": "𝑑",
    "e": "𝑒",
    "f": "𝑓",
    "g": "𝑔",
    "h": "ℎ",
    "i": "𝑖",
    "j": "𝑗",
    "k": "𝑘",
    "l": "𝑙",
    "m": "𝑚",
    "n": "𝑛",
    "o": "𝑜",
    "p": "𝑝",
    "q": "𝑞",
    "r": "𝑟",
    "s": "𝑠",
    "t": "𝑡",
    "u": "𝑢",
    "v": "𝑣",
    "w": "𝑤",
    "x": "𝑥",
    "y": "𝑦",
    "z": "𝑧",
    "Α": "𝛢",
    "Β": "𝛣",
    "Γ": "𝛤",
    "Δ": "𝛥",
    "Ε": "𝛦",
    "Ζ": "𝛧",
    "Η": "𝛨",
    "Θ": "𝛩",
    "Ι": "𝛪",
    "Κ": "𝛫",
    "Λ": "𝛬",
    "Μ": "𝛭",
    "Ν": "𝛮",
    "Ξ": "𝛯",
    "Ο": "𝛰",
    "Π": "𝛱",
    "Ρ": "𝛲",
    "ϴ": "𝛳",
    "Σ": "𝛴",
    "Τ": "𝛵",
    "Υ": "𝛶",
    "Φ": "𝛷",
    "Χ": "𝛸",
    "Ψ": "𝛹",
    "Ω": "𝛺",
    "∇": "𝛻",
    "α": "𝛼",
    "β": "𝛽",
    "γ": "𝛾",
    "δ": "𝛿",
    "ε": "𝜀",
    "ζ": "𝜁",
    "η": "𝜂",
    "θ": "𝜃",
    "ι": "𝜄",
    "κ": "𝜅",
    "λ": "𝜆",
    "μ": "𝜇",
    "ν": "𝜈",
    "ξ": "𝜉",
    "ο": "𝜊",
    "π": "𝜋",
    "ρ": "𝜌",
    "ς": "𝜍",
    "σ": "𝜎",
    "τ": "𝜏",
    "υ": "𝜐",
    "φ": "𝜑",
    "χ": "𝜒",
    "ψ": "𝜓",
    "ω": "𝜔",
    "∂": "𝜕",
    "ϵ": "𝜖",
    "ϑ": "𝜗",
    "ϰ": "𝜘",
    "ϕ": "𝜙",
    "ϱ": "𝜚",
    "ϖ": "𝜛",
}

mono = {
    "A": "𝙰",
    "B": "𝙱",
    "C": "𝙲",
    "D": "𝙳",
    "E": "𝙴",
    "F": "𝙵",
    "G": "𝙶",
    "H": "𝙷",
    "I": "𝙸",
    "J": "𝙹",
    "K": "𝙺",
    "L": "𝙻",
    "M": "𝙼",
    "N": "𝙽",
    "O": "𝙾",
    "P": "𝙿",
    "Q": "𝚀",
    "R": "𝚁",
    "S": "𝚂",
    "T": "𝚃",
    "U": "𝚄",
    "V": "𝚅",
    "W": "𝚆",
    "X": "𝚇",
    "Y": "𝚈",
    "Z": "𝚉",
    "a": "𝚊",
    "b": "𝚋",
    "c": "𝚌",
    "d": "𝚍",
    "e": "𝚎",
    "f": "𝚏",
    "g": "𝚐",
    "h": "𝚑",
    "i": "𝚒",
    "j": "𝚓",
    "k": "𝚔",
    "l": "𝚕",
    "m": "𝚖",
    "n": "𝚗",
    "o": "𝚘",
    "p": "𝚙",
    "q": "𝚚",
    "r": "𝚛",
    "s": "𝚜",
    "t": "𝚝",
    "u": "𝚞",
    "v": "𝚟",
    "w": "𝚠",
    "x": "𝚡",
    "y": "𝚢",
    "z": "𝚣",
    "0": "𝟶",
    "1": "𝟷",
    "2": "𝟸",
    "3": "𝟹",
    "4": "𝟺",
    "5": "𝟻",
    "6": "𝟼",
    "7": "𝟽",
    "8": "𝟾",
    "9": "𝟿",
}

transliterators = {
    r"\bb": bb,
    r"\bf": bf,
    r"\cal": cal,
    r"\frak": frak,
    r"\it": it,
    r"\mono": mono,
}


symbols = {
    r"\_": "_",
    r"\|": "‖",
    r"\lVert": "‖",
    r"\rVert": "‖",
    r"\\": "\\",
    r"\aleph": "ℵ",
    r"\alpha": "α",
    r"\amalg": "∐",
    r"\angle": "∠",
    r"\approx": "≈",
    r"\approxeq": "≊",
    r"\ast": "∗",
    r"\asymp": "≍",
    r"\backsim": "∽",
    r"\backsimeq": "⋍",
    r"\backslash": "\\",
    r"\barwedge": "⊼",
    r"\because": "∵",
    r"\beta": "β",
    r"\beth": "ℶ",
    r"\between": "≬",
    r"\bigcap": "⋂",
    r"\bigcup": "⋃",
    r"\bigvee": "⋁",
    r"\bigwedge": "⋀",
    r"\blacksquare": "∎",
    r"\bot": "⊤",
    r"\bowtie": "⋈",
    r"\boxdot": "⊡",
    r"\boxminus": "⊟",
    r"\boxplus": "⊞",
    r"\boxtimes": "⊠",
    r"\bullet": "•",
    r"\bumpeq": "≏",
    r"\Bumpeq": "≎",
    r"\cap": "∩",
    r"\Cap": "⋒",
    r"\cdot": "·",
    r"\cdots": "⋯",
    r"\chi": "χ",
    r"\circ": "∘",
    r"\circeq": "≗",
    r"\circlearrowleft": "↺",
    r"\circlearrowright": "↻",
    r"\circledast": "⊛",
    r"\circledcirc": "⊚",
    r"\circleddash": "⊝",
    r"\clubsuit": "♣",
    r"\varclubsuit": "♧",
    r"\complement": "∁",
    r"\cong": "≅",
    r"\cup": "∪",
    r"\Cup": "⋓",
    r"\curlyeqprec": "⋞",
    r"\curlyeqsucc": "⋟",
    r"\curlyvee": "⋎",
    r"\curlywedge": "⋏",
    r"\curvearrowleft": "↶",
    r"\curvearrowright": "↷",
    r"\dag": "†",
    r"\daleth": "ℸ",
    r"\dashleftarrow": "⇠",
    r"\dashrightarrow": "⇢",
    r"\dashv": "⊣",
    r"\ddag": "‡",
    r"\ddots": "⋱",
    r"\ddotsup": "⋰",
    r"\defeq": "≝",
    r"\delta": "δ",
    r"\Delta": "Δ",
    r"\diamond": "⋄",
    r"\diamondsuit": "♢",
    r"\vardiamondsuit": "♦",
    r"\div": "÷",
    r"\divideontimes": "⋇",
    r"\doteq": "≐",
    r"\doteqdot": "≑",
    r"\dotplus": "∔",
    r"\dots": "…",
    r"\downarrow": "↓",
    r"\Downarrow": "⇓",
    r"\downdownarrows": "⇊",
    r"\downharpoonleft": "⇃",
    r"\downharpoonright": "⇂",
    r"\ell": "ℓ",
    r"\emptyset": "∅",
    r"\epsilon": "ϵ",
    r"\eqcirc": "≖",
    r"\eqslantgtr": "⋝",
    r"\eqslantless": "⋜",
    r"\equiv": "≡",
    r"\eta": "η",
    r"\exists": "∃",
    r"\fallingdotseq": "≒",
    r"\Finv": "Ⅎ",
    r"\flat": "♭",
    r"\forall": "∀",
    r"\gamma": "γ",
    r"\Gamma": "Γ",
    r"\geq": "≥",
    r"\geqq": "≧",
    r"\gg": "≫",
    r"\ggg": "⋙",
    r"\gimel": "ℷ",
    r"\gneqq": "≩",
    r"\gnsim": "⋧",
    r"\gtrdot": "⋗",
    r"\gtreqless": "⋛",
    r"\gtrless": "≷",
    r"\gtrsim": "≳",
    r"\hbar": "ℏ",
    r"\heartsuit": "♡",
    r"\varheartsuit": "♥",
    r"\hookleftarrow": "↩",
    r"\hookrightarrow": "↪",
    r"\iiint": "∭",
    r"\iint": "∬",
    r"\Im": "ℑ",
    r"\in": "∈",
    r"\infty": "∞",
    r"\int": "∫",
    r"\intercal": "⊺",
    r"\iota": "ι",
    r"\kappa": "κ",
    r"\lambda": "λ",
    r"\Lambda": "Λ",
    r"\leadsto": "↝",
    r"\leftarrow": "←",
    r"\Leftarrow": "⇐",
    r"\leftarrowtail": "↢",
    r"\leftharpoondown": "↽",
    r"\leftharpoonup": "↼",
    r"\leftleftarrows": "⇇",
    r"\leftrightarrow": "↔",
    r"\Leftrightarrow": "⇔",
    r"\leftrightarrows": "⇆",
    r"\leftrightharpoons": "⇋",
    r"\leftrightsquigarrow": "↭",
    r"\leftthreetimes": "⋋",
    r"\leq": "≤",
    r"\leqq": "≦",
    r"\lessdot": "⋖",
    r"\lesseqgtr": "⋚",
    r"\lessgtr": "≶",
    r"\lesssim": "≲",
    r"\lhd": "⊲",
    r"\ll": "≪",
    r"\Lleftarrow": "⇚",
    r"\lll": "⋘",
    r"\lneqq": "≨",
    r"\lnot": "¬",
    r"\neg": "¬",
    r"\lnsim": "⋦",
    r"\looparrowleft": "↫",
    r"\looparrowright": "↬",
    r"\Lsh": "↰",
    r"\ltimes": "⋉",
    r"\mapsto": "↦",
    r"\measuredangle": "∡",
    r"\mho": "℧",
    r"\mid": "∣",
    r"\models": "⊨",
    r"\mp": "∓",
    r"\multimap": "⊸",
    r"\multimapdotbothA": "⊶",
    r"\multimapdotbothB": "⊷",
    r"\mu": "μ",
    r"\nabla": "∇",
    r"\natural": "♮",
    r"\ncong": "≇",
    r"\nearrow": "↗",
    r"\neq": "≠",
    r"\nexists": "∄",
    r"\ngeq": "≱",
    r"\ngtr": "≯",
    r"\ni": "∋",
    r"\nleftarrow": "↚",
    r"\nLeftarrow": "⇍",
    r"\nleftrightarrow": "↮",
    r"\nLeftrightarrow": "⇎",
    r"\nleq": "≰",
    r"\nless": "≮",
    r"\nmid": "∤",
    r"\notin": "∉",
    r"\nparallel": "∦",
    r"\nprec": "⊁",
    r"\nrightarrow": "↛",
    r"\nRightarrow": "⇏",
    r"\nsim": "≁",
    r"\nsubseteq": "⊈",
    r"\nsucc": "⊀",
    r"\nsupseteq": "⊉",
    r"\ntriangleleft": "⋪",
    r"\ntrianglelefteq": "⋬",
    r"\ntriangleright": "⋫",
    r"\ntrianglerighteq": "⋭",
    r"\nu": "ν",
    r"\nvdash": "⊬",
    r"\nvDash": "⊭",
    r"\nVdash": "⊯",
    r"\nwarrow": "↖",
    r"\odot": "⊙",
    r"\oiiint": "∰",
    r"\oiint": "∯",
    r"\oint": "∮",
    r"\omega": "ω",
    r"\Omega": "Ω",
    r"\ominus": "⊖",
    r"\oplus": "⊕",
    r"\oslash": "⊘",
    r"\otimes": "⊗",
    r"\P": "¶",
    r"\parallel": "∥",
    r"\partial": "∂",
    r"\perp": "⊥",
    r"\phi": "ϕ",
    r"\Phi": "Φ",
    r"\pitchfork": "⋔",
    r"\pi": "π",
    r"\Pi": "Π",
    r"\pm": "±",
    r"\pounds": "£",
    r"\prec": "≺",
    r"\preccurlyeq": "≼",
    r"\precnsim": "⋨",
    r"\precsim": "≾",
    r"\prod": "∏",
    r"\propto": "∝",
    r"\psi": "ψ",
    r"\Psi": "Ψ",
    r"\Re": "ℜ",
    r"\rhd": "⊳",
    r"\rho": "ρ",
    r"\rightarrow": "→",
    r"\Rightarrow": "⇒",
    r"\rightarrowtail": "↣",
    r"\rightharpoondown": "⇁",
    r"\rightharpoonup": "⇀",
    r"\rightleftarrows": "⇄",
    r"\rightleftharpoons": "⇌",
    r"\rightrightarrows": "⇉",
    r"\rightsquigarrow": "⇝",
    r"\rightthreetimes": "⋌",
    r"\risingdotseq": "≓",
    r"\Rsh": "↱",
    r"\rtimes": "⋊",
    r"\S": "§",
    r"\searrow": "↘",
    r"\swarrow": "↙",
    r"\setminus": "∖",
    r"\sharp": "♯",
    r"\sigma": "σ",
    r"\Sigma": "Σ",
    r"\sim": "∼",
    r"\simeq": "≃",
    r"\spadesuit": "♠",
    r"\varspadesuit": "♤",
    r"\sphericalangle": "∢",
    r"\sqcap": "⊓",
    r"\sqcup": "⊔",
    r"\sqsubset": "⊏",
    r"\sqsubseteq": "⊑",
    r"\sqsupset": "⊐",
    r"\sqsupseteq": "⊒",
    r"\star": "⋆",
    r"\subset": "⊂",
    r"\Subset": "⋐",
    r"\subseteq": "⊆",
    r"\subsetneq": "⊊",
    r"\succ": "≻",
    r"\succcurlyeq": "≽",
    r"\succnsim": "⋩",
    r"\succsim": "≿",
    r"\sum": "∑",
    r"\supset": "⊃",
    r"\Supset": "⋑",
    r"\supseteq": "⊇",
    r"\supsetneq": "⊋",
    r"\surd": "√",
    r"\tau": "τ",
    r"\therefore": "∴",
    r"\theta": "θ",
    r"\Theta": "Θ",
    r"\times": "×",
    r"\triangleq": "≜",
    r"\twoheadleftarrow": "↞",
    r"\twoheadrightarrow": "↠",
    r"\unlhd": "⊴",
    r"\unrhd": "⊵",
    r"\uparrow": "↑",
    r"\Uparrow": "⇑",
    r"\updownarrow": "↕",
    r"\Updownarrow": "⇕",
    r"\upharpoonleft": "↿",
    r"\upharpoonright": "↾",
    r"\uplus": "⊎",
    r"\upsilon": "υ",
    r"\upuparrows": "⇈",
    r"\varepsilon": "ε",
    r"\varphi": "φ",
    r"\varpi": "ϖ",
    r"\varrho": "ϱ",
    r"\varsigma": "ς",
    r"\vartheta": "ϑ",
    r"\vdash": "⊢",
    r"\vDash": "⊧",
    r"\Vdash": "⊩",
    r"\vdots": "⋮",
    r"\vee": "∨",
    r"\veebar": "⊻",
    r"\Vvdash": "⊪",
    r"\wedge": "∧",
    r"\wp": "℘",
    r"\wr": "≀",
    r"\xi": "ξ",
    r"\Xi": "Ξ",
    r"\zeta": "ζ",
    r"\ ": " ",
    r"\,": " ",
    r"\;": "  ",
    r"\quad": "   ",
    r"\qquad": "    ",
}

combinings = {
    r"\hat": ("\u0302", "hat"),
    r"\grave": ("\u0300", "grave"),
    r"\dot": ("\u0307", "dot"),
    r"\not": ("\u0338", "not"),
    r"\overrightarrow": ("\u20d7", "overrightarrow"),
    r"\overline": ("\u0305", "overline"),
    r"\tilde": ("\u0303", "tilde"),
    r"\bar": ("\u0304", "bar"),
    r"\acute": ("\u0301", "acute"),
    r"\ddot": ("\u0308", "ddot"),
    r"\overleftarrow": ("\u20d6", "overleftarrow"),
    r"\check": ("\u030c", "check"),
    r"\vec": ("\u20d7", "vec"),
    r"\underline": ("\u0332", "underline"),
}

newcommands = (
    r"\newcommand\mathcal[1]{\cal{#1}}",
    r"\newcommand\mathit[1]{\it{#1}}",
    r"\newcommand\mathbf[1]{\bf{#1}}",
    r"\newcommand\mathbb[1]{\bb{#1}}",
    r"\newcommand\mathmono[1]{\mono{#1}}",
    r"\newcommand\mathfrak[1]{\frak{#1}}",
    r"\newcommand\binom[2]{binom(#1,#2)}",
    r"\newcommand\'[1]{\acute{#1}}",
    r"\newcommand\`[1]{\grave{#1}}",
    r"\newcommand\^[1]{\hat{#1}}",
    r"\newcommand\widehat[1]{\hat{#1}}",
)
