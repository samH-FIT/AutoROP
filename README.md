# AutoROP
This tool is intended to automate the usage of ROPgadget for building ROP chains and exploiting vulnerable server binaries. While still useful for larger projects, it's primary purpose is for CTF pwn challenges.

## Installation and Usage
1. `git clone https://github.com/samH-FIT/AutoROP.git`
2. `cd AutoROP`
3. `python [SCRIPT] [BINARY] [HOST] [PORT]`

## TODO
* Add in a cyclic feature for automating the process of finding the necessary padding to overflow the target binary (32-bit only).
* Add in an option for local or remote exploitation.
