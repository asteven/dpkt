# $Id$

"""Internet Group Management Protocol."""

import dpkt

class IGMP(dpkt.Packet):
    __hdr__ = (
        ('type', 'B', 0),
        ('maxresp', 'B', 0),
        ('sum', 'H', 0),
        ('group', 'I', 0)
        )
    def __str__(self):
        if not self.sum:
            self.sum = dpkt.in_cksum(dpkt.Packet.__str__(self))
        return dpkt.Packet.__str__(self)
