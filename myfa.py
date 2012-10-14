#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys

ZWNJ = u'\u200c'
ZWJ = u'\u200d'

code_data = (
    (u'ا', 'a'),
    (u'آ', 'a1'),
    (u'اً', 'a2'),
    (u'ب', 'c'),
    (u'پ', 'c3'),
    (u'ت', 'c1'),
    (u'ث', 'c2'),
    (u'ج', 'z1'),
    (u'چ', 'z3'),
    (u'ح', 'z'),
    (u'خ', 'z2'),
    (u'د', 'v'),
    (u'ذ', 'v1'),
    (u'ر', 'h'),
    (u'ز', 'h1'),
    (u'ژ', 'h3'),
    (u'س', 'w'),
    (u'ش', 'w3'),
    (u'ص', 'g'),
    (u'ض', 'g1'),
    (u'ط', 'b'),
    (u'ظ', 'b1'),
    (u'ع', 'e'),
    (u'غ', 'e1'),
    (u'ف', 'j1'),
    (u'ق', 'g2'),
    (u'ک', 'y1'),
    (u'گ', 'y2'),
    (u'ل', 'j'),
    (u'م', 'p'),
    (u'ن', 'n'),
    (u'و', 'q'),
    (u'ه', 'o'),
    (u'هٔ', 'o2'),
    (u'ی', 'y'),
    (u'ئ', 'y3'),
    (ZWNJ, '-'),
)

fa2code = dict(code_data)
code2fa = dict([(fa, c) for c, fa in code_data])

#faSet = set(fa2code.keys())
#codeSet = set(fa2code.values())


toStr = lambda s: s.encode('utf8') if isinstance(s, unicode) else str(s)
toUnicode = lambda s: s if isinstance(s, unicode) else str(s).decode('utf8')


def transFa2code(text):
    ctext = u''
    for c in toUnicode(text):
        try:
            c = fa2code[c]
        except KeyError:
            pass
        ctext += c
    return ctext.replace(u'aً', u'a2').replace(u'oٔ', u'o2')

def transCode2fa(ctext):
    ctext = toUnicode(ctext)
    clen = len(ctext)
    text = u''
    i = 0
    while i < clen:
        c = ctext[i]
        try:
            cn = ctext[i+1]
        except IndexError:
            cn = None
        cf = u''
        if cn in (u'1', u'2', u'3'):
            try:
                cf = code2fa[c + cn]
            except KeyError:
                cf = c + cn
            i += 2
        else:
            try:
                cf = code2fa[c]
            except KeyError:
                cf = c
            i += 1
        text += cf
    return text


if __name__=='__main__':
    if sys.argv[1] == '-p':## print
        for fa, code in code_data:
            print '%s\t%s'%(toStr(fa), toStr(code))
    elif sys.argv[1] == '-f':## file
        print toStr(transFa2code(open(sys.argv[2]).read()))
    elif sys.argv[1] == '-fd':## file
        print toStr(transCode2fa(open(sys.argv[2]).read()))
    elif sys.argv[1] == '-d':## decode
        print toStr(transCode2fa(' '.join(sys.argv[2:])))
    else:
        print toStr(transFa2code(' '.join(sys.argv[1:])))





