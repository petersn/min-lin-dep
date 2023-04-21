import hashlib, struct

hashes = []
for i in range(2**16):
    b = struct.pack("<H", i)
    h = hashlib.sha256(b).digest()
    h = ''.join('{:08b}'.format(x) for x in h)
    hashes.append(h)

# We now construct a SAT instance.

import autosat


