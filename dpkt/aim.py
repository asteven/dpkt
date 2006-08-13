# $Id: aim.py 271 2006-01-11 16:03:33Z dugsong $

"""AOL Instant Messenger."""

import dpkt
import struct

# OSCAR: http://iserverd1.khstu.ru/oscar/

class FLAP(dpkt.Packet):
    __hdr__ = [
        ('ast', 'B', ord('*')),
        ('type', 'B', 0),
        ('seq', 'H', 0),
        ('len', 'H', 0)
    ]

class SNAC(dpkt.Packet):
    __hdr__ = [
        ('family', 'H', 0),
        ('subtype', 'H', 0),
        ('flags', 'H', 0),
        ('reqid', 'I', 0)
        ]

def tlv(buf):
    n = 4
    t, l = struct.unpack('>HH', buf[:n])
    v = buf[n:n+l]
    buf = buf[n+l:]
    return (t,l,v, buf)

# TOC 1.0: http://jamwt.com/Py-TOC/PROTOCOL

# TOC 2.0: http://www.firestuff.org/projects/firetalk/doc/toc2.txt

