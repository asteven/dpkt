# $Id: loopback.py 271 2006-01-11 16:03:33Z dugsong $

"""Platform-dependent loopback header."""

import dpkt, ethernet, ip, ip6

class Loopback(dpkt.Packet):
    __hdr__ = (('family', 'I', 0), )
    def unpack(self, buf):
        dpkt.Packet.unpack(self, buf)
        if self.family > 1500:
            self.data = ethernet.Ethernet(self.data)
        else:
            v = ord(self.data[0]) >> 4
            if self.family == 2 or v == 4:
                # AF_INET appears consistent
                self.data = ip.IP(self.data)
            elif v == 6:
                # XXX - AF_INET6 differs on *BSD, MacOS X, etc.
                self.data = ip6.IP6(self.data)

