# $Id$

"""Portmap / rpcbind."""

import dpkt

PMAP_PROG = 100000L
PMAP_PROCDUMP = 4
PMAP_VERS = 2

class Pmap(dpkt.Packet):
    __hdr__ = (
        ('prog', 'I', 0),
        ('vers', 'I', 0),
        ('prot', 'I', 0),
        ('port', 'I', 0),
        )
