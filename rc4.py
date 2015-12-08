#!/usr/bin/env python
#
#       rc4.py - RC4, ARC4, ARCFOUR algorithm (with random salt removed)
#
#       Copyright (c) 2009 joonis new media
#       Author: Thimo Kraemer <thimo.kraemer@joonis.de>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#

__all__ = ['crypt', 'encrypt', 'decrypt']


def crypt(data, key):
    z = 1
    x = 0
    box = range(256)
    for i in range(256):
        x = (x + box[i] + ord(key[i % len(key)])) % 256
        box[i], box[x] = box[x], box[i]
    x = y = 0
    out = []
    for char in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]

        # the following lines were modified to extract the first byte generated
        out_char = box[(box[x] + box[y]) % 256]
        if z == 1:
            first_byte = hex(out_char)
            z = 0
        out.append(chr(ord(char) ^ out_char))  # box[(box[x] + box[y]) % 256]))

    return ''.join(out), first_byte


def encrypt(data, key):
    data = crypt(data, key)
    return data


def decrypt(data, key):
    return crypt(data, key)
