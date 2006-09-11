# $Id: mrt.py 271 2006-01-11 16:03:33Z jonojono $

"""Multi-threaded Routing Toolkit."""

import dpkt

# Multi-threaded Routing Toolkit
# http://www.ietf.org/internet-drafts/draft-ietf-grow-mrt-03.txt

# MRT Types
NULL			= 0
START			= 1
DIE			= 2
I_AM_DEAD		= 3
PEER_DOWN		= 4
BGP			= 5	# Deprecated by BGP4MP
RIP			= 6
IDRP			= 7
RIPNG			= 8
BGP4PLUS		= 9	# Deprecated by BGP4MP
BGP4PLUS_01		= 10	# Deprecated by BGP4MP
OSPF			= 11
TABLE_DUMP		= 12
BGP4MP			= 16
BGP4MP_ET		= 17
ISIS			= 32
ISIS_ET			= 33
OSPF_ET			= 64

# BGP4MP Subtypes
BGP4MP_STATE_CHANGE	= 0
BGP4MP_MESSAGE		= 1
BGP4MP_ENTRY		= 2
BGP4MP_SNAPSHOT		= 3
BGP4MP_MESSAGE_32BIT_AS	= 4

# Address Family Types
AFI_IPv4		= 1
AFI_IPv6		= 2

class MRTHeader(dpkt.Packet):
    __hdr__ = (
        ('ts', 'I', 0),
        ('type', 'H', 0),
        ('subtype', 'H', 0),
        ('len', 'I', 0)
        )

class BGP4MPMessage(dpkt.Packet):
    __hdr__ = (
        ('src_as', 'H', 0),
        ('dst_as', 'H', 0),
        ('intf', 'H', 0),
        ('family', 'H', AFI_IPv4),
        ('src_ip', 'I', 0),
        ('dst_ip', 'I', 0)
        )
