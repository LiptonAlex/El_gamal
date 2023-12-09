import Crypto.Util.number
from Crypto import Random
import Crypto
import random
import libnum
import sys
import hashlib


def primitive_root(p_val: int) -> int:
    while True:
        g = random.randrange(3, p_val)
        if pow(g, 2, p_val) == 1:
            continue
        if pow(g, p_val, p_val) == 1:
            continue
        return g


bits = 2048
M = "Hello World!"

if (len(sys.argv) > 1):
    M = sys.argv[1]
if (len(sys.argv) > 2):
    bits = int(sys.argv[2])

p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

m = int.from_bytes(M.encode(), byteorder='big')

g = primitive_root(p)
x1 = random.randrange(3, p)
Y1 = pow(g, x1, p)
x2 = random.randrange(3, p)
Y2 = pow(g, x2, p)

r1 = random.randrange(3, p)
r2 = random.randrange(3, p)

print(f"Message: {M}")
print(f"Bob's Public key: g={g}, Y={Y1}, p={p}\nBob's Private key: x={x1}, r1={r1}")
print(f"\nAlice's Public key: g={g}, Y={Y2}, p={p}\nAlice's Private key: x={x2}, r2={r2}")

c11 = pow(g, r1, p)
c21 = (pow(Y1, r1, p) * m) % p

c12 = pow(g, r2, p)
c22 = (pow(Y2, r2, p) * c21) % p

print(f"\nEncrypted\nc11={c11}\nc12={c12}\nc22={c22}\n")

print("First removing Alice's key then Bob's")
Alice_remove = (c22 * libnum.invmod(pow(c12, x2, p), p)) % p
M_recovered = (Alice_remove * libnum.invmod(pow(c11, x1, p), p)) % p

m_rec = int.to_bytes(M_recovered, len(M), byteorder='big')

print(f"\nResult: {m_rec.decode()}\n")

print("First removing Bob's key then Alice's")
Bob_remove = (c22 * libnum.invmod(pow(c11, x1, p), p)) % p
M_recovered = (Bob_remove * libnum.invmod(pow(c12, x2, p), p)) % p

m_rec = int.to_bytes(M_recovered, len(M), byteorder='big')

print(f"\nResult: {m_rec.decode()}")
