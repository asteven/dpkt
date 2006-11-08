# $Id$

"""Encapsulated Security Protocol."""

import dpkt

class ESP(dpkt.Packet):
    __hdr__ = (
        ('spi', 'I', 0),
        ('seq', 'I', 0)
        )
