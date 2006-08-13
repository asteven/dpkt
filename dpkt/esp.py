# $Id: esp.py 290 2006-01-22 02:43:28Z dugsong $

"""Encapsulated Security Protocol."""

import dpkt

class ESP(dpkt.Packet):
    __hdr__ = (
        ('spi', 'I', 0),
        ('seq', 'I', 0)
        )
