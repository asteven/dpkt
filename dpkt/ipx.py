# $Id: ipx.py 358 2006-04-21 20:11:25Z dugsong $

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
