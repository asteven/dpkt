# $Id$

"""Internetwork Packet Exchange."""

import dpkt

IPX_HDR_LEN = 30

class IPX(dpkt.Packet):
    __hdr__ = (
        ('sum', 'H', 0xffff),
        ('len', 'H', IPX_HDR_LEN),
        ('tc', 'B', 0),
        ('pt', 'B', 0),
        ('dst', '12s', ''),
        ('src', '12s', '')
        )
