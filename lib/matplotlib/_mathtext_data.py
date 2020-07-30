"""
font data tables for truetype and afm computer modern fonts
"""

latex_to_cmex = {
    r'\__sqrt__'   : 0x70,
    r'\bigcap'     : 0x5c,
    r'\bigcup'     : 0x5b,
    r'\bigodot'    : 0x4b,
    r'\bigoplus'   : 0x4d,
    r'\bigotimes'  : 0x4f,
    r'\biguplus'   : 0x5d,
    r'\bigvee'     : 0x5f,
    r'\bigwedge'   : 0x5e,
    r'\coprod'     : 0x61,
    r'\int'        : 0x5a,
    r'\leftangle'  : 0xad,
    r'\leftbrace'  : 0xa9,
    r'\oint'       : 0x49,
    r'\prod'       : 0x59,
    r'\rightangle' : 0xae,
    r'\rightbrace' : 0xaa,
    r'\sum'        : 0x58,
    r'\widehat'    : 0x62,
    r'\widetilde'  : 0x65,
}

latex_to_bakoma = {
    ','                          : ('cmmi10', 0x3b),
    '.'                          : ('cmmi10', 0x3a),
    '/'                          : ('cmmi10', 0x3d),
    '\\imath'                    : ('cmmi10', 0x7b),
    '\\jmath'                    : ('cmmi10', 0x7c),

    '!'                          : ('cmr10', 0x21),
    '%'                          : ('cmr10', 0x25),
    '&'                          : ('cmr10', 0x26),
    '('                          : ('cmr10', 0x28),
    ')'                          : ('cmr10', 0x29),
    '+'                          : ('cmr10', 0x2b),
    '0'                          : ('cmr10', 0x30),
    '1'                          : ('cmr10', 0x31),
    '2'                          : ('cmr10', 0x32),
    '3'                          : ('cmr10', 0x33),
    '4'                          : ('cmr10', 0x34),
    '5'                          : ('cmr10', 0x35),
    '6'                          : ('cmr10', 0x36),
    '7'                          : ('cmr10', 0x37),
    '8'                          : ('cmr10', 0x38),
    '9'                          : ('cmr10', 0x39),
    ':'                          : ('cmr10', 0x3a),
    ';'                          : ('cmr10', 0x3b),
    '='                          : ('cmr10', 0x3d),
    '?'                          : ('cmr10', 0x3f),
    '@'                          : ('cmr10', 0x40),
    '['                          : ('cmr10', 0x5b),
    '\\#'                        : ('cmr10', 0x23),
    '\\$'                        : ('cmr10', 0x24),
    '\\%'                        : ('cmr10', 0x25),
    '\\Delta'                    : ('cmr10', 0xa2),
    '\\Gamma'                    : ('cmr10', 0xa1),
    '\\Lambda'                   : ('cmr10', 0xa4),
    '\\Omega'                    : ('cmr10', 0xad),
    '\\Phi'                      : ('cmr10', 0xa9),
    '\\Pi'                       : ('cmr10', 0xa6),
    '\\Psi'                      : ('cmr10', 0xaa),
    '\\Sigma'                    : ('cmr10', 0xa7),
    '\\Theta'                    : ('cmr10', 0xa3),
    '\\Upsilon'                  : ('cmr10', 0xa8),
    '\\Xi'                       : ('cmr10', 0xa5),
    '\\circumflexaccent'         : ('cmr10', 0x5e),
    '\\combiningacuteaccent'     : ('cmr10', 0xb6),
    '\\combiningbreve'           : ('cmr10', 0xb8),
    '\\combiningdiaeresis'       : ('cmr10', 0xc4),
    '\\combiningdotabove'        : ('cmr10', 0x5f),
    '\\combininggraveaccent'     : ('cmr10', 0xb5),
    '\\combiningoverline'        : ('cmr10', 0xb9),
    '\\combiningtilde'           : ('cmr10', 0x7e),
    '\\leftbracket'              : ('cmr10', 0x5b),
    '\\leftparen'                : ('cmr10', 0x28),
    '\\rightbracket'             : ('cmr10', 0x5d),
    '\\rightparen'               : ('cmr10', 0x29),
    '\\widebar'                  : ('cmr10', 0xb9),
    ']'                          : ('cmr10', 0x5d),
}

latex_to_standard = {
    '\\#'                        : ('pncr8a', 35),
    '\\$'                        : ('pncr8a', 36),
    '\\%'                        : ('pncr8a', 37),
    '\\ast'                      : ('pncr8a', 42),
    '\\backslash'                : ('pncr8a', 92),
    '\\{'                        : ('pncr8a', 123),
    '\\}'                        : ('pncr8a', 125),
    '\\imath'                    : ('pncri8a', 105),
    '\\combininggraveaccent'     : ('pncri8a', 193),  # \grave
    '\\combiningacuteaccent'     : ('pncri8a', 194),  # \acute
    '\\circumflexaccent'         : ('pncri8a', 195),  # \hat
    '\\combiningtilde'           : ('pncri8a', 196),  # \tilde
    '\\combiningbreve'           : ('pncri8a', 198),  # \breve
    '\\combiningdotabove'        : ('pncri8a', 199),  # \dot
    '\\combiningdiaeresis'       : ('pncri8a', 200),  # \ddot
    '\\sharp'                    : ('psyr', 35),
    '\\leftparen'                : ('psyr', 40),
    '\\rightparen'               : ('psyr', 41),
    '\\slash'                    : ('psyr', 47),
    '\\leftbracket'              : ('psyr', 91),
    '\\rightbracket'             : ('psyr', 93),
    '\\mu'                       : ('psyr', 109),
    '\\lbrace'                   : ('psyr', 123),
    '\\leftbrace'                : ('psyr', 123),
    '\\rbrace'                   : ('psyr', 125),
    '\\rightbrace'               : ('psyr', 125),
    '\\leftrightarrow'           : ('psyr', 171),
    '\\leftarrow'                : ('psyr', 172),
    '\\uparrow'                  : ('psyr', 173),
    '\\combiningrightarrowabove' : ('psyr', 174),     # \vec
    '\\rightarrow'               : ('psyr', 174),
    '\\to'                       : ('psyr', 174),
    '\\downarrow'                : ('psyr', 175),
    '\\circ'                     : ('psyr', 176),
    '\\pm'                       : ('psyr', 176),
    '\\times'                    : ('psyr', 180),
    '\\bullet'                   : ('psyr', 183),
    '\\div'                      : ('psyr', 184),
    '\\ldots'                    : ('psyr', 188),
    '\\neg'                      : ('psyr', 216),
    '\\urcorner'                 : ('psyr', 216),
}

uni2type1 = {
    **dict(zip(
        [c for c in range(256) if chr(c).isprintable()],
        # 0x2_
        'space exclam quotedbl numbersign '
        'dollar percent ampersand quotesingle '
        'parenleft parenright asterisk plus '
        'comma hyphen period slash '
        # 0x3_
        'zero one two three four five six seven '
        'eight nine colon semicolon less equal greater question '
        # 0x4_
        'at A B C D E F G H I J K L M N O '
        # 0x5_
        'P Q R S T U V W '
        'X Y Z bracketleft backslash bracketright asciicircum underscore '
        # 0x6_
        'grave a b c d e f g h i j k l m n o '
        # 0x7_ (0x7f: delete)
        'p q r s t u v w x y z braceleft bar braceright asciitilde '
        # 0xa_ (0xa0: non-breaking space, 0xad: soft hyphen)
        ' exclamdown cent sterling '
        'currency yen brokenbar section '
        'dieresis copyright ordfeminine guillemotleft '
        'logicalnot  registered macron '
        # 0xb_
        'degree plusminus twosuperior threesuperior '
        'acute mu paragraph periodcentered '
        'cedilla onesuperior ordmasculine guillemotright '
        'onequarter onehalf threequarters questiondown '
        # 0xc_
        'Agrave Aacute Acircumflex Atilde '
        'Adieresis Aring AE Ccedilla '
        'Egrave Eacute Ecircumflex Edieresis '
        'Igrave Iacute Icircumflex Idieresis '
        # 0xd_
        'Eth Ntilde Ograve Oacute '
        'Ocircumflex Otilde Odieresis multiply '
        'Oslash Ugrave Uacute Ucircumflex '
        'Udieresis Yacute Thorn germandbls '
        # 0xe_
        'agrave aacute acircumflex atilde '
        'adieresis aring ae ccedilla '
        'egrave eacute ecircumflex edieresis '
        'igrave iacute icircumflex idieresis '
        # 0xf_
        'eth ntilde ograve oacute '
        'ocircumflex otilde odieresis divide '
        'oslash ugrave uacute ucircumflex '
        'udieresis yacute thorn ydieresis'
        .split())),
    0x0130: 'Idot',
    0x0131: 'dotlessi',
    0x0132: 'IJ',
    0x0133: 'ij',
    0x0141: 'Lslash',
    0x0142: 'lslash',
    0x0152: 'OE',
    0x0153: 'oe',
    0x015e: 'Scedilla',
    0x015f: 'scedilla',
    0x0160: 'Scaron',
    0x0161: 'scaron',
    0x0178: 'Ydieresis',
    0x017d: 'Zcaron',
    0x017e: 'zcaron',
    0x0192: 'florin',
    0x01e6: 'Gcaron',
    0x01e7: 'gcaron',
    0x02c6: 'circumflex',
    0x02c7: 'caron',
    0x02d8: 'breve',
    0x02d9: 'dotaccent',
    0x02da: 'ring',
    0x02db: 'ogonek',
    0x02dc: 'tilde',
    0x02dd: 'hungarumlaut',
    0x0391: 'Alpha',
    0x0392: 'Beta',
    0x0393: 'Gamma',
    0x0395: 'Epsilon',
    0x0396: 'Zeta',
    0x0397: 'Eta',
    0x0398: 'Theta',
    0x0399: 'Iota',
    0x039a: 'Kappa',
    0x039b: 'Lambda',
    0x039c: 'Mu',
    0x039d: 'Nu',
    0x039e: 'Xi',
    0x039f: 'Omicron',
    0x03a0: 'Pi',
    0x03a1: 'Rho',
    0x03a3: 'Sigma',
    0x03a4: 'Tau',
    0x03a5: 'Upsilon',
    0x03a6: 'Phi',
    0x03a7: 'Chi',
    0x03a8: 'Psi',
    0x03b1: 'alpha',
    0x03b2: 'beta',
    0x03b3: 'gamma',
    0x03b4: 'delta',
    0x03b5: 'epsilon',
    0x03b6: 'zeta',
    0x03b7: 'eta',
    0x03b8: 'theta',
    0x03b9: 'iota',
    0x03ba: 'kappa',
    0x03bb: 'lambda',
    0x03bd: 'nu',
    0x03be: 'xi',
    0x03bf: 'omicron',
    0x03c0: 'pi',
    0x03c1: 'rho',
    0x03c2: 'sigma1',
    0x03c3: 'sigma',
    0x03c4: 'tau',
    0x03c5: 'upsilon',
    0x03c6: 'phi',
    0x03c7: 'chi',
    0x03c8: 'psi',
    0x03c9: 'omega',
    0x03d1: 'theta1',
    0x03d2: 'Upsilon1',
    0x03d5: 'phi1',
    0x03d6: 'omega1',
    0x2013: 'endash',
    0x2014: 'emdash',
    0x2018: 'quoteleft',
    0x2019: 'quoteright',
    0x201a: 'quotesinglbase',
    0x201c: 'quotedblleft',
    0x201d: 'quotedblright',
    0x201e: 'quotedblbase',
    0x2020: 'dagger',
    0x2021: 'daggerdbl',
    0x2022: 'bullet',
    0x2026: 'ellipsis',
    0x2030: 'perthousand',
    0x2032: 'minute',
    0x2033: 'second',
    0x2039: 'guilsinglleft',
    0x203a: 'guilsinglright',
    0x2044: 'fraction',
    0x20a4: 'lira',
    0x2111: 'Ifraktur',
    0x2118: 'weierstrass',
    0x211c: 'Rfraktur',
    0x211e: 'prescription',
    0x2122: 'trademark',
    0x2126: 'Omega',
    0x2135: 'aleph',
    0x2190: 'arrowleft',
    0x2191: 'arrowup',
    0x2192: 'arrowright',
    0x2193: 'arrowdown',
    0x2194: 'arrowboth',
    0x21b5: 'carriagereturn',
    0x21d0: 'arrowdblleft',
    0x21d1: 'arrowdblup',
    0x21d2: 'arrowdblright',
    0x21d3: 'arrowdbldown',
    0x21d4: 'arrowdblboth',
    0x2200: 'universal',
    0x2202: 'partialdiff',
    0x2203: 'existential',
    0x2205: 'emptyset',
    0x2206: 'Delta',
    0x2207: 'nabla',
    0x2207: 'gradient',
    0x2208: 'element',
    0x2209: 'notelement',
    0x220b: 'suchthat',
    0x220f: 'product',
    0x2211: 'summation',
    0x2212: 'minus',
    0x2213: 'minusplus',
    0x2217: 'asteriskmath',
    0x221a: 'radical',
    0x221d: 'proportional',
    0x221e: 'infinity',
    0x2220: 'angle',
    0x2227: 'logicaland',
    0x2228: 'logicalor',
    0x2229: 'intersection',
    0x222a: 'union',
    0x222b: 'integral',
    0x2234: 'therefore',
    0x223c: 'similar',
    0x2245: 'congruent',
    0x2248: 'approxequal',
    0x2260: 'notequal',
    0x2261: 'equivalence',
    0x2264: 'lessequal',
    0x2265: 'greaterequal',
    0x227a: 'precedes',
    0x2282: 'propersubset',
    0x2283: 'propersuperset',
    0x2284: 'notsubset',
    0x2286: 'reflexsubset',
    0x2287: 'reflexsuperset',
    0x2295: 'circleplus',
    0x2297: 'circlemultiply',
    0x22a5: 'perpendicular',
    0x22c5: 'dotmath',
    0x2320: 'integraltp',
    0x2321: 'integralbt',
    0x2329: 'angleleft',
    0x232a: 'angleright',
    0x25ca: 'lozenge',
    0x25e6: 'openbullet',
    0x2660: 'spade',
    0x2663: 'club',
    0x2665: 'heart',
    0x2666: 'diamond',
    0xf6be: 'dotlessj',
    0xf6bf: 'LL',
    0xf6c0: 'll',
    0xf6d9: 'copyrightserif',
    0xf6da: 'registerserif',
    0xf6db: 'trademarkserif',
    0xf730: 'zerooldstyle',
    0xf731: 'oneoldstyle',
    0xf732: 'twooldstyle',
    0xf733: 'threeoldstyle',
    0xf734: 'fouroldstyle',
    0xf735: 'fiveoldstyle',
    0xf736: 'sixoldstyle',
    0xf737: 'sevenoldstyle',
    0xf738: 'eightoldstyle',
    0xf739: 'nineoldstyle',
    0xf8e5: 'radicalex',
    0xf8e6: 'arrowvertex',
    0xf8e7: 'arrowhorizex',
    0xf8e8: 'registersans',
    0xf8e9: 'copyrightsans',
    0xf8ea: 'trademarksans',
    0xf8eb: 'parenlefttp',
    0xf8ec: 'parenleftex',
    0xf8ed: 'parenleftbt',
    0xf8ee: 'bracketlefttp',
    0xf8ef: 'bracketleftex',
    0xf8f0: 'bracketleftbt',
    0xf8f1: 'bracelefttp',
    0xf8f2: 'braceleftmid',
    0xf8f3: 'braceleftbt',
    0xf8f4: 'braceex',
    0xf8f5: 'integralex',
    0xf8f6: 'parenrighttp',
    0xf8f7: 'parenrightex',
    0xf8f8: 'parenrightbt',
    0xf8f9: 'bracketrighttp',
    0xf8fa: 'bracketrightex',
    0xf8fb: 'bracketrightbt',
    0xf8fc: 'bracerighttp',
    0xf8fd: 'bracerightmid',
    0xf8fe: 'bracerightbt',
    0xf8ff: 'apple',
    0xfb00: 'ff',
    0xfb01: 'fi',
    0xfb02: 'fl',
    0xfb03: 'ffi',
    0xfb04: 'ffl',
}

# Automatically generated.

tex2uni = {
    'widehat'                  : 0x0302,
    'widetilde'                : 0x0303,
    'widebar'                  : 0x0305,
    'langle'                   : 0x27e8,
    'rangle'                   : 0x27e9,
    'perp'                     : 0x27c2,
    'neq'                      : 0x2260,
    'Join'                     : 0x2a1d,
    'leqslant'                 : 0x2a7d,
    'geqslant'                 : 0x2a7e,
    'lessapprox'               : 0x2a85,
    'gtrapprox'                : 0x2a86,
    'lesseqqgtr'               : 0x2a8b,
    'gtreqqless'               : 0x2a8c,
    'triangleeq'               : 0x225c,
    'eqslantless'              : 0x2a95,
    'eqslantgtr'               : 0x2a96,
    'backepsilon'              : 0x03f6,
    'precapprox'               : 0x2ab7,
    'succapprox'               : 0x2ab8,
    'fallingdotseq'            : 0x2252,
    'subseteqq'                : 0x2ac5,
    'supseteqq'                : 0x2ac6,
    'varpropto'                : 0x221d,
    'precnapprox'              : 0x2ab9,
    'succnapprox'              : 0x2aba,
    'subsetneqq'               : 0x2acb,
    'supsetneqq'               : 0x2acc,
    'lnapprox'                 : 0x2ab9,
    'gnapprox'                 : 0x2aba,
    'longleftarrow'            : 0x27f5,
    'longrightarrow'           : 0x27f6,
    'longleftrightarrow'       : 0x27f7,
    'Longleftarrow'            : 0x27f8,
    'Longrightarrow'           : 0x27f9,
    'Longleftrightarrow'       : 0x27fa,
    'longmapsto'               : 0x27fc,
    'leadsto'                  : 0x21dd,
    'dashleftarrow'            : 0x290e,
    'dashrightarrow'           : 0x290f,
    'circlearrowleft'          : 0x21ba,
    'circlearrowright'         : 0x21bb,
    'leftrightsquigarrow'      : 0x21ad,
    'leftsquigarrow'           : 0x219c,
    'rightsquigarrow'          : 0x219d,
    'Game'                     : 0x2141,
    'hbar'                     : 0x0127,
    'hslash'                   : 0x210f,
    'ldots'                    : 0x2026,
    'vdots'                    : 0x22ee,
    'doteqdot'                 : 0x2251,
    'doteq'                    : 8784,
    'partial'                  : 8706,
    'gg'                       : 8811,
    'asymp'                    : 8781,
    'blacktriangledown'        : 9662,
    'otimes'                   : 8855,
    'nearrow'                  : 8599,
    'varpi'                    : 982,
    'vee'                      : 8744,
    'vec'                      : 8407,
    'smile'                    : 8995,
    'succnsim'                 : 8937,
    'gimel'                    : 8503,
    'vert'                     : 124,
    '|'                        : 124,
    'varrho'                   : 1009,
    'P'                        : 182,
    'approxident'              : 8779,
    'Swarrow'                  : 8665,
    'textasciicircum'          : 94,
    'imageof'                  : 8887,
    'ntriangleleft'            : 8938,
    'nleq'                     : 8816,
    'div'                      : 247,
    'nparallel'                : 8742,
    'Leftarrow'                : 8656,
    'lll'                      : 8920,
    'oiint'                    : 8751,
    'ngeq'                     : 8817,
    'Theta'                    : 920,
    'origof'                   : 8886,
    'blacksquare'              : 9632,
    'solbar'                   : 9023,
    'neg'                      : 172,
    'sum'                      : 8721,
    'Vdash'                    : 8873,
    'coloneq'                  : 8788,
    'degree'                   : 176,
    'bowtie'                   : 8904,
    'blacktriangleright'       : 9654,
    'varsigma'                 : 962,
    'leq'                      : 8804,
    'ggg'                      : 8921,
    'lneqq'                    : 8808,
    'scurel'                   : 8881,
    'stareq'                   : 8795,
    'BbbN'                     : 8469,
    'nLeftarrow'               : 8653,
    'nLeftrightarrow'          : 8654,
    'k'                        : 808,
    'bot'                      : 8869,
    'BbbC'                     : 8450,
    'Lsh'                      : 8624,
    'leftleftarrows'           : 8647,
    'BbbZ'                     : 8484,
    'digamma'                  : 989,
    'BbbR'                     : 8477,
    'BbbP'                     : 8473,
    'BbbQ'                     : 8474,
    'vartriangleright'         : 8883,
    'succsim'                  : 8831,
    'wedge'                    : 8743,
    'lessgtr'                  : 8822,
    'veebar'                   : 8891,
    'mapsdown'                 : 8615,
    'Rsh'                      : 8625,
    'chi'                      : 967,
    'prec'                     : 8826,
    'nsubseteq'                : 8840,
    'therefore'                : 8756,
    'eqcirc'                   : 8790,
    'textexclamdown'           : 161,
    'nRightarrow'              : 8655,
    'flat'                     : 9837,
    'notin'                    : 8713,
    'llcorner'                 : 8990,
    'varepsilon'               : 949,
    'bigtriangleup'            : 9651,
    'aleph'                    : 8501,
    'dotminus'                 : 8760,
    'upsilon'                  : 965,
    'Lambda'                   : 923,
    'cap'                      : 8745,
    'barleftarrow'             : 8676,
    'mu'                       : 956,
    'boxplus'                  : 8862,
    'mp'                       : 8723,
    'circledast'               : 8859,
    'tau'                      : 964,
    'in'                       : 8712,
    'backslash'                : 92,
    'varnothing'               : 8709,
    'sharp'                    : 9839,
    'eqsim'                    : 8770,
    'gnsim'                    : 8935,
    'Searrow'                  : 8664,
    'updownarrows'             : 8645,
    'heartsuit'                : 9825,
    'trianglelefteq'           : 8884,
    'ddag'                     : 8225,
    'sqsubseteq'               : 8849,
    'mapsfrom'                 : 8612,
    'boxbar'                   : 9707,
    'sim'                      : 8764,
    'Nwarrow'                  : 8662,
    'nequiv'                   : 8802,
    'succ'                     : 8827,
    'vdash'                    : 8866,
    'Leftrightarrow'           : 8660,
    'parallel'                 : 8741,
    'invnot'                   : 8976,
    'natural'                  : 9838,
    'ss'                       : 223,
    'uparrow'                  : 8593,
    'nsim'                     : 8769,
    'hookrightarrow'           : 8618,
    'Equiv'                    : 8803,
    'approx'                   : 8776,
    'Vvdash'                   : 8874,
    'nsucc'                    : 8833,
    'leftrightharpoons'        : 8651,
    'Re'                       : 8476,
    'boxminus'                 : 8863,
    'equiv'                    : 8801,
    'Lleftarrow'               : 8666,
    'll'                       : 8810,
    'Cup'                      : 8915,
    'measeq'                   : 8798,
    'upharpoonleft'            : 8639,
    'lq'                       : 8216,
    'Upsilon'                  : 933,
    'subsetneq'                : 8842,
    'greater'                  : 62,
    'supsetneq'                : 8843,
    'Cap'                      : 8914,
    'L'                        : 321,
    'spadesuit'                : 9824,
    'lrcorner'                 : 8991,
    'not'                      : 824,
    'bar'                      : 772,
    'rightharpoonaccent'       : 8401,
    'boxdot'                   : 8865,
    'l'                        : 322,
    'leftharpoondown'          : 8637,
    'bigcup'                   : 8899,
    'iint'                     : 8748,
    'bigwedge'                 : 8896,
    'downharpoonleft'          : 8643,
    'textasciitilde'           : 126,
    'subset'                   : 8834,
    'leqq'                     : 8806,
    'mapsup'                   : 8613,
    'nvDash'                   : 8877,
    'looparrowleft'            : 8619,
    'nless'                    : 8814,
    'rightarrowbar'            : 8677,
    'Vert'                     : 8214,
    'downdownarrows'           : 8650,
    'uplus'                    : 8846,
    'simeq'                    : 8771,
    'napprox'                  : 8777,
    'ast'                      : 8727,
    'twoheaduparrow'           : 8607,
    'doublebarwedge'           : 8966,
    'Sigma'                    : 931,
    'leftharpoonaccent'        : 8400,
    'ntrianglelefteq'          : 8940,
    'nexists'                  : 8708,
    'times'                    : 215,
    'measuredangle'            : 8737,
    'bumpeq'                   : 8783,
    'carriagereturn'           : 8629,
    'adots'                    : 8944,
    'checkmark'                : 10003,
    'lambda'                   : 955,
    'xi'                       : 958,
    'rbrace'                   : 125,
    'rbrack'                   : 93,
    'Nearrow'                  : 8663,
    'maltese'                  : 10016,
    'clubsuit'                 : 9827,
    'top'                      : 8868,
    'overarc'                  : 785,
    'varphi'                   : 966,
    'Delta'                    : 916,
    'iota'                     : 953,
    'nleftarrow'               : 8602,
    'candra'                   : 784,
    'supset'                   : 8835,
    'triangleleft'             : 9665,
    'gtreqless'                : 8923,
    'ntrianglerighteq'         : 8941,
    'quad'                     : 8195,
    'Xi'                       : 926,
    'gtrdot'                   : 8919,
    'leftthreetimes'           : 8907,
    'minus'                    : 8722,
    'preccurlyeq'              : 8828,
    'nleftrightarrow'          : 8622,
    'lambdabar'                : 411,
    'blacktriangle'            : 9652,
    'kernelcontraction'        : 8763,
    'Phi'                      : 934,
    'angle'                    : 8736,
    'spadesuitopen'            : 9828,
    'eqless'                   : 8924,
    'mid'                      : 8739,
    'varkappa'                 : 1008,
    'Ldsh'                     : 8626,
    'updownarrow'              : 8597,
    'beta'                     : 946,
    'textquotedblleft'         : 8220,
    'rho'                      : 961,
    'alpha'                    : 945,
    'intercal'                 : 8890,
    'beth'                     : 8502,
    'grave'                    : 768,
    'acwopencirclearrow'       : 8634,
    'nmid'                     : 8740,
    'nsupset'                  : 8837,
    'sigma'                    : 963,
    'dot'                      : 775,
    'Rightarrow'               : 8658,
    'turnednot'                : 8985,
    'backsimeq'                : 8909,
    'leftarrowtail'            : 8610,
    'approxeq'                 : 8778,
    'curlyeqsucc'              : 8927,
    'rightarrowtail'           : 8611,
    'Psi'                      : 936,
    'copyright'                : 169,
    'yen'                      : 165,
    'vartriangleleft'          : 8882,
    'rasp'                     : 700,
    'triangleright'            : 9655,
    'precsim'                  : 8830,
    'infty'                    : 8734,
    'geq'                      : 8805,
    'updownarrowbar'           : 8616,
    'precnsim'                 : 8936,
    'H'                        : 779,
    'ulcorner'                 : 8988,
    'looparrowright'           : 8620,
    'ncong'                    : 8775,
    'downarrow'                : 8595,
    'circeq'                   : 8791,
    'subseteq'                 : 8838,
    'bigstar'                  : 9733,
    'prime'                    : 8242,
    'lceil'                    : 8968,
    'Rrightarrow'              : 8667,
    'oiiint'                   : 8752,
    'curlywedge'               : 8911,
    'vDash'                    : 8872,
    'lfloor'                   : 8970,
    'ddots'                    : 8945,
    'exists'                   : 8707,
    'underbar'                 : 817,
    'Pi'                       : 928,
    'leftrightarrows'          : 8646,
    'sphericalangle'           : 8738,
    'coprod'                   : 8720,
    'circledcirc'              : 8858,
    'gtrsim'                   : 8819,
    'gneqq'                    : 8809,
    'between'                  : 8812,
    'theta'                    : 952,
    'complement'               : 8705,
    'arceq'                    : 8792,
    'nVdash'                   : 8878,
    'S'                        : 167,
    'wr'                       : 8768,
    'wp'                       : 8472,
    'backcong'                 : 8780,
    'lasp'                     : 701,
    'c'                        : 807,
    'nabla'                    : 8711,
    'dotplus'                  : 8724,
    'eta'                      : 951,
    'forall'                   : 8704,
    'eth'                      : 240,
    'colon'                    : 58,
    'sqcup'                    : 8852,
    'rightrightarrows'         : 8649,
    'sqsupset'                 : 8848,
    'mapsto'                   : 8614,
    'bigtriangledown'          : 9661,
    'sqsupseteq'               : 8850,
    'propto'                   : 8733,
    'pi'                       : 960,
    'pm'                       : 177,
    'dots'                     : 0x2026,
    'nrightarrow'              : 8603,
    'textasciiacute'           : 180,
    'Doteq'                    : 8785,
    'breve'                    : 774,
    'sqcap'                    : 8851,
    'twoheadrightarrow'        : 8608,
    'kappa'                    : 954,
    'vartriangle'              : 9653,
    'diamondsuit'              : 9826,
    'pitchfork'                : 8916,
    'blacktriangleleft'        : 9664,
    'nprec'                    : 8832,
    'curvearrowright'          : 8631,
    'barwedge'                 : 8892,
    'multimap'                 : 8888,
    'textquestiondown'         : 191,
    'cong'                     : 8773,
    'rtimes'                   : 8906,
    'rightzigzagarrow'         : 8669,
    'rightarrow'               : 8594,
    'leftarrow'                : 8592,
    '__sqrt__'                 : 8730,
    'twoheaddownarrow'         : 8609,
    'oint'                     : 8750,
    'bigvee'                   : 8897,
    'eqdef'                    : 8797,
    'sterling'                 : 163,
    'phi'                      : 981,
    'Updownarrow'              : 8661,
    'backprime'                : 8245,
    'emdash'                   : 8212,
    'Gamma'                    : 915,
    'i'                        : 305,
    'rceil'                    : 8969,
    'leftharpoonup'            : 8636,
    'Im'                       : 8465,
    'curvearrowleft'           : 8630,
    'wedgeq'                   : 8793,
    'curlyeqprec'              : 8926,
    'questeq'                  : 8799,
    'less'                     : 60,
    'upuparrows'               : 8648,
    'tilde'                    : 771,
    'textasciigrave'           : 96,
    'smallsetminus'            : 8726,
    'ell'                      : 8467,
    'cup'                      : 8746,
    'danger'                   : 9761,
    'nVDash'                   : 8879,
    'cdotp'                    : 183,
    'cdots'                    : 8943,
    'hat'                      : 770,
    'eqgtr'                    : 8925,
    'psi'                      : 968,
    'frown'                    : 8994,
    'acute'                    : 769,
    'downzigzagarrow'          : 8623,
    'ntriangleright'           : 8939,
    'cupdot'                   : 8845,
    'circleddash'              : 8861,
    'oslash'                   : 8856,
    'mho'                      : 8487,
    'd'                        : 803,
    'sqsubset'                 : 8847,
    'cdot'                     : 8901,
    'Omega'                    : 937,
    'OE'                       : 338,
    'veeeq'                    : 8794,
    'Finv'                     : 8498,
    't'                        : 865,
    'leftrightarrow'           : 8596,
    'swarrow'                  : 8601,
    'rightthreetimes'          : 8908,
    'rightleftharpoons'        : 8652,
    'lesssim'                  : 8818,
    'searrow'                  : 8600,
    'because'                  : 8757,
    'gtrless'                  : 8823,
    'star'                     : 8902,
    'nsubset'                  : 8836,
    'zeta'                     : 950,
    'dddot'                    : 8411,
    'bigcirc'                  : 9675,
    'Supset'                   : 8913,
    'circ'                     : 8728,
    'slash'                    : 8725,
    'ocirc'                    : 778,
    'prod'                     : 8719,
    'twoheadleftarrow'         : 8606,
    'daleth'                   : 8504,
    'upharpoonright'           : 8638,
    'odot'                     : 8857,
    'Uparrow'                  : 8657,
    'O'                        : 216,
    'hookleftarrow'            : 8617,
    'trianglerighteq'          : 8885,
    'nsime'                    : 8772,
    'oe'                       : 339,
    'nwarrow'                  : 8598,
    'o'                        : 248,
    'ddddot'                   : 8412,
    'downharpoonright'         : 8642,
    'succcurlyeq'              : 8829,
    'gamma'                    : 947,
    'scrR'                     : 8475,
    'dag'                      : 8224,
    'thickspace'               : 8197,
    'frakZ'                    : 8488,
    'lessdot'                  : 8918,
    'triangledown'             : 9663,
    'ltimes'                   : 8905,
    'scrB'                     : 8492,
    'endash'                   : 8211,
    'scrE'                     : 8496,
    'scrF'                     : 8497,
    'scrH'                     : 8459,
    'scrI'                     : 8464,
    'rightharpoondown'         : 8641,
    'scrL'                     : 8466,
    'scrM'                     : 8499,
    'frakC'                    : 8493,
    'nsupseteq'                : 8841,
    'circledR'                 : 174,
    'circledS'                 : 9416,
    'ngtr'                     : 8815,
    'bigcap'                   : 8898,
    'scre'                     : 8495,
    'Downarrow'                : 8659,
    'scrg'                     : 8458,
    'overleftrightarrow'       : 8417,
    'scro'                     : 8500,
    'lnsim'                    : 8934,
    'eqcolon'                  : 8789,
    'curlyvee'                 : 8910,
    'urcorner'                 : 8989,
    'lbrace'                   : 123,
    'Bumpeq'                   : 8782,
    'delta'                    : 948,
    'boxtimes'                 : 8864,
    'overleftarrow'            : 8406,
    'prurel'                   : 8880,
    'clubsuitopen'             : 9831,
    'cwopencirclearrow'        : 8635,
    'geqq'                     : 8807,
    'rightleftarrows'          : 8644,
    'ac'                       : 8766,
    'ae'                       : 230,
    'int'                      : 8747,
    'rfloor'                   : 8971,
    'risingdotseq'             : 8787,
    'nvdash'                   : 8876,
    'diamond'                  : 8900,
    'ddot'                     : 776,
    'backsim'                  : 8765,
    'oplus'                    : 8853,
    'triangleq'                : 8796,
    'check'                    : 780,
    'ni'                       : 8715,
    'iiint'                    : 8749,
    'ne'                       : 8800,
    'lesseqgtr'                : 8922,
    'obar'                     : 9021,
    'supseteq'                 : 8839,
    'nu'                       : 957,
    'AA'                       : 197,
    'AE'                       : 198,
    'models'                   : 8871,
    'ominus'                   : 8854,
    'dashv'                    : 8867,
    'omega'                    : 969,
    'rq'                       : 8217,
    'Subset'                   : 8912,
    'rightharpoonup'           : 8640,
    'Rdsh'                     : 8627,
    'bullet'                   : 8729,
    'divideontimes'            : 8903,
    'lbrack'                   : 91,
    'textquotedblright'        : 8221,
    'Colon'                    : 8759,
    '%'                        : 37,
    '$'                        : 36,
    '{'                        : 123,
    '}'                        : 125,
    '_'                        : 95,
    '#'                        : 35,
    'imath'                    : 0x131,
    'circumflexaccent'         : 770,
    'combiningbreve'           : 774,
    'combiningoverline'        : 772,
    'combininggraveaccent'     : 768,
    'combiningacuteaccent'     : 769,
    'combiningdiaeresis'       : 776,
    'combiningtilde'           : 771,
    'combiningrightarrowabove' : 8407,
    'combiningdotabove'        : 775,
    'to'                       : 8594,
    'succeq'                   : 8829,
    'emptyset'                 : 8709,
    'leftparen'                : 40,
    'rightparen'               : 41,
    'bigoplus'                 : 10753,
    'leftangle'                : 10216,
    'rightangle'               : 10217,
    'leftbrace'                : 124,
    'rightbrace'               : 125,
    'jmath'                    : 567,
    'bigodot'                  : 10752,
    'preceq'                   : 8828,
    'biguplus'                 : 10756,
    'epsilon'                  : 949,
    'vartheta'                 : 977,
    'bigotimes'                : 10754,
    'guillemotleft'            : 171,
    'ring'                     : 730,
    'Thorn'                    : 222,
    'guilsinglright'           : 8250,
    'perthousand'              : 8240,
    'macron'                   : 175,
    'cent'                     : 162,
    'guillemotright'           : 187,
    'equal'                    : 61,
    'asterisk'                 : 42,
    'guilsinglleft'            : 8249,
    'plus'                     : 43,
    'thorn'                    : 254,
    'dagger'                   : 8224
}

# Each element is a 4-tuple of the form:
#   src_start, src_end, dst_font, dst_start
#
stix_virtual_fonts = {
    'bb':
        {
        'rm':
            [
            (0x0030, 0x0039, 'rm', 0x1d7d8), # 0-9
            (0x0041, 0x0042, 'rm', 0x1d538), # A-B
            (0x0043, 0x0043, 'rm', 0x2102),  # C
            (0x0044, 0x0047, 'rm', 0x1d53b), # D-G
            (0x0048, 0x0048, 'rm', 0x210d),  # H
            (0x0049, 0x004d, 'rm', 0x1d540), # I-M
            (0x004e, 0x004e, 'rm', 0x2115),  # N
            (0x004f, 0x004f, 'rm', 0x1d546), # O
            (0x0050, 0x0051, 'rm', 0x2119),  # P-Q
            (0x0052, 0x0052, 'rm', 0x211d),  # R
            (0x0053, 0x0059, 'rm', 0x1d54a), # S-Y
            (0x005a, 0x005a, 'rm', 0x2124),  # Z
            (0x0061, 0x007a, 'rm', 0x1d552), # a-z
            (0x0393, 0x0393, 'rm', 0x213e),  # \Gamma
            (0x03a0, 0x03a0, 'rm', 0x213f),  # \Pi
            (0x03a3, 0x03a3, 'rm', 0x2140),  # \Sigma
            (0x03b3, 0x03b3, 'rm', 0x213d),  # \gamma
            (0x03c0, 0x03c0, 'rm', 0x213c),  # \pi
            ],
        'it':
            [
            (0x0030, 0x0039, 'rm', 0x1d7d8), # 0-9
            (0x0041, 0x0042, 'it', 0xe154),  # A-B
            (0x0043, 0x0043, 'it', 0x2102),  # C
            (0x0044, 0x0044, 'it', 0x2145),  # D
            (0x0045, 0x0047, 'it', 0xe156),  # E-G
            (0x0048, 0x0048, 'it', 0x210d),  # H
            (0x0049, 0x004d, 'it', 0xe159),  # I-M
            (0x004e, 0x004e, 'it', 0x2115),  # N
            (0x004f, 0x004f, 'it', 0xe15e),  # O
            (0x0050, 0x0051, 'it', 0x2119),  # P-Q
            (0x0052, 0x0052, 'it', 0x211d),  # R
            (0x0053, 0x0059, 'it', 0xe15f),  # S-Y
            (0x005a, 0x005a, 'it', 0x2124),  # Z
            (0x0061, 0x0063, 'it', 0xe166),  # a-c
            (0x0064, 0x0065, 'it', 0x2146),  # d-e
            (0x0066, 0x0068, 'it', 0xe169),  # f-h
            (0x0069, 0x006a, 'it', 0x2148),  # i-j
            (0x006b, 0x007a, 'it', 0xe16c),  # k-z
            (0x0393, 0x0393, 'it', 0x213e),  # \Gamma (not in beta STIX fonts)
            (0x03a0, 0x03a0, 'it', 0x213f),  # \Pi
            (0x03a3, 0x03a3, 'it', 0x2140),  # \Sigma (not in beta STIX fonts)
            (0x03b3, 0x03b3, 'it', 0x213d),  # \gamma (not in beta STIX fonts)
            (0x03c0, 0x03c0, 'it', 0x213c),  # \pi
            ],
        'bf':
            [
            (0x0030, 0x0039, 'rm', 0x1d7d8), # 0-9
            (0x0041, 0x0042, 'bf', 0xe38a),  # A-B
            (0x0043, 0x0043, 'bf', 0x2102),  # C
            (0x0044, 0x0044, 'bf', 0x2145),  # D
            (0x0045, 0x0047, 'bf', 0xe38d),  # E-G
            (0x0048, 0x0048, 'bf', 0x210d),  # H
            (0x0049, 0x004d, 'bf', 0xe390),  # I-M
            (0x004e, 0x004e, 'bf', 0x2115),  # N
            (0x004f, 0x004f, 'bf', 0xe395),  # O
            (0x0050, 0x0051, 'bf', 0x2119),  # P-Q
            (0x0052, 0x0052, 'bf', 0x211d),  # R
            (0x0053, 0x0059, 'bf', 0xe396),  # S-Y
            (0x005a, 0x005a, 'bf', 0x2124),  # Z
            (0x0061, 0x0063, 'bf', 0xe39d),  # a-c
            (0x0064, 0x0065, 'bf', 0x2146),  # d-e
            (0x0066, 0x0068, 'bf', 0xe3a2),  # f-h
            (0x0069, 0x006a, 'bf', 0x2148),  # i-j
            (0x006b, 0x007a, 'bf', 0xe3a7),  # k-z
            (0x0393, 0x0393, 'bf', 0x213e),  # \Gamma
            (0x03a0, 0x03a0, 'bf', 0x213f),  # \Pi
            (0x03a3, 0x03a3, 'bf', 0x2140),  # \Sigma
            (0x03b3, 0x03b3, 'bf', 0x213d),  # \gamma
            (0x03c0, 0x03c0, 'bf', 0x213c),  # \pi
            ],
        },
    'cal':
        [
        (0x0041, 0x005a, 'it', 0xe22d), # A-Z
        ],
    'frak':
        {
        'rm':
            [
            (0x0041, 0x0042, 'rm', 0x1d504), # A-B
            (0x0043, 0x0043, 'rm', 0x212d),  # C
            (0x0044, 0x0047, 'rm', 0x1d507), # D-G
            (0x0048, 0x0048, 'rm', 0x210c),  # H
            (0x0049, 0x0049, 'rm', 0x2111),  # I
            (0x004a, 0x0051, 'rm', 0x1d50d), # J-Q
            (0x0052, 0x0052, 'rm', 0x211c),  # R
            (0x0053, 0x0059, 'rm', 0x1d516), # S-Y
            (0x005a, 0x005a, 'rm', 0x2128),  # Z
            (0x0061, 0x007a, 'rm', 0x1d51e), # a-z
            ],
        'it':
            [
            (0x0041, 0x0042, 'rm', 0x1d504), # A-B
            (0x0043, 0x0043, 'rm', 0x212d),  # C
            (0x0044, 0x0047, 'rm', 0x1d507), # D-G
            (0x0048, 0x0048, 'rm', 0x210c),  # H
            (0x0049, 0x0049, 'rm', 0x2111),  # I
            (0x004a, 0x0051, 'rm', 0x1d50d), # J-Q
            (0x0052, 0x0052, 'rm', 0x211c),  # R
            (0x0053, 0x0059, 'rm', 0x1d516), # S-Y
            (0x005a, 0x005a, 'rm', 0x2128),  # Z
            (0x0061, 0x007a, 'rm', 0x1d51e), # a-z
            ],
        'bf':
            [
            (0x0041, 0x005a, 'bf', 0x1d56c), # A-Z
            (0x0061, 0x007a, 'bf', 0x1d586), # a-z
            ],
        },
    'scr':
        [
        (0x0041, 0x0041, 'it', 0x1d49c), # A
        (0x0042, 0x0042, 'it', 0x212c),  # B
        (0x0043, 0x0044, 'it', 0x1d49e), # C-D
        (0x0045, 0x0046, 'it', 0x2130),  # E-F
        (0x0047, 0x0047, 'it', 0x1d4a2), # G
        (0x0048, 0x0048, 'it', 0x210b),  # H
        (0x0049, 0x0049, 'it', 0x2110),  # I
        (0x004a, 0x004b, 'it', 0x1d4a5), # J-K
        (0x004c, 0x004c, 'it', 0x2112),  # L
        (0x004d, 0x004d, 'it', 0x2133),  # M
        (0x004e, 0x0051, 'it', 0x1d4a9), # N-Q
        (0x0052, 0x0052, 'it', 0x211b),  # R
        (0x0053, 0x005a, 'it', 0x1d4ae), # S-Z
        (0x0061, 0x0064, 'it', 0x1d4b6), # a-d
        (0x0065, 0x0065, 'it', 0x212f),  # e
        (0x0066, 0x0066, 'it', 0x1d4bb), # f
        (0x0067, 0x0067, 'it', 0x210a),  # g
        (0x0068, 0x006e, 'it', 0x1d4bd), # h-n
        (0x006f, 0x006f, 'it', 0x2134),  # o
        (0x0070, 0x007a, 'it', 0x1d4c5), # p-z
        ],
    'sf':
        {
        'rm':
            [
            (0x0030, 0x0039, 'rm', 0x1d7e2), # 0-9
            (0x0041, 0x005a, 'rm', 0x1d5a0), # A-Z
            (0x0061, 0x007a, 'rm', 0x1d5ba), # a-z
            (0x0391, 0x03a9, 'rm', 0xe17d),  # \Alpha-\Omega
            (0x03b1, 0x03c9, 'rm', 0xe196),  # \alpha-\omega
            (0x03d1, 0x03d1, 'rm', 0xe1b0),  # theta variant
            (0x03d5, 0x03d5, 'rm', 0xe1b1),  # phi variant
            (0x03d6, 0x03d6, 'rm', 0xe1b3),  # pi variant
            (0x03f1, 0x03f1, 'rm', 0xe1b2),  # rho variant
            (0x03f5, 0x03f5, 'rm', 0xe1af),  # lunate epsilon
            (0x2202, 0x2202, 'rm', 0xe17c),  # partial differential
            ],
        'it':
            [
            # These numerals are actually upright.  We don't actually
            # want italic numerals ever.
            (0x0030, 0x0039, 'rm', 0x1d7e2), # 0-9
            (0x0041, 0x005a, 'it', 0x1d608), # A-Z
            (0x0061, 0x007a, 'it', 0x1d622), # a-z
            (0x0391, 0x03a9, 'rm', 0xe17d),  # \Alpha-\Omega
            (0x03b1, 0x03c9, 'it', 0xe1d8),  # \alpha-\omega
            (0x03d1, 0x03d1, 'it', 0xe1f2),  # theta variant
            (0x03d5, 0x03d5, 'it', 0xe1f3),  # phi variant
            (0x03d6, 0x03d6, 'it', 0xe1f5),  # pi variant
            (0x03f1, 0x03f1, 'it', 0xe1f4),  # rho variant
            (0x03f5, 0x03f5, 'it', 0xe1f1),  # lunate epsilon
            ],
        'bf':
            [
            (0x0030, 0x0039, 'bf', 0x1d7ec), # 0-9
            (0x0041, 0x005a, 'bf', 0x1d5d4), # A-Z
            (0x0061, 0x007a, 'bf', 0x1d5ee), # a-z
            (0x0391, 0x03a9, 'bf', 0x1d756), # \Alpha-\Omega
            (0x03b1, 0x03c9, 'bf', 0x1d770), # \alpha-\omega
            (0x03d1, 0x03d1, 'bf', 0x1d78b), # theta variant
            (0x03d5, 0x03d5, 'bf', 0x1d78d), # phi variant
            (0x03d6, 0x03d6, 'bf', 0x1d78f), # pi variant
            (0x03f0, 0x03f0, 'bf', 0x1d78c), # kappa variant
            (0x03f1, 0x03f1, 'bf', 0x1d78e), # rho variant
            (0x03f5, 0x03f5, 'bf', 0x1d78a), # lunate epsilon
            (0x2202, 0x2202, 'bf', 0x1d789), # partial differential
            (0x2207, 0x2207, 'bf', 0x1d76f), # \Nabla
            ],
        },
    'tt':
        [
        (0x0030, 0x0039, 'rm', 0x1d7f6), # 0-9
        (0x0041, 0x005a, 'rm', 0x1d670), # A-Z
        (0x0061, 0x007a, 'rm', 0x1d68a)  # a-z
        ],
    }
