import zlib

s = b'witch which has which witches wrist watch'
print(len(s))

t = zlib.compress(s)
print(len(t))

decompressed = zlib.decompress(t)
print(decompressed)

crc32 = zlib.crc32(s)
print(crc32)