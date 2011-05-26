#!/usr/bin/env python

from packing import pack, unpack

def check(fmt, *v):
	print fmt, repr(v), ''.join('%02x' % ord(c) for c in pack(fmt, *v))

check('iii', 0, 101, -99)
check('3i', 0, 101, -99)
check('iS', 42, "forty two")
check('u', r"\x42" * 20)
check('uu', r"\x42" * 10, r"\x42" * 10)
