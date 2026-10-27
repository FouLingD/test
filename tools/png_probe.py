import struct, zlib, sys

path = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else None

data = open(path, "rb").read()
assert data[:8] == b"\x89PNG\r\n\x1a\n"

pos = 8
idat = b""
w = h = bitd = ct = None
while pos < len(data):
    ln = struct.unpack(">I", data[pos:pos+4])[0]
    typ = data[pos+4:pos+8]
    body = data[pos+8:pos+8+ln]
    pos += 12 + ln
    if typ == b"IHDR":
        w, h, bitd, ct = struct.unpack(">IIBB", body[:10])
    elif typ == b"IDAT":
        idat += body
    elif typ == b"IEND":
        break

raw = zlib.decompress(idat)
ch = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}[ct]
stride = w * ch

rows = []
prev = bytearray(stride)
p = 0
for y in range(h):
    ft = raw[p]
    p += 1
    line = bytearray(raw[p:p+stride])
    p += stride
    if ft == 0:
        pass
    elif ft == 1:
        for i in range(ch, stride):
            line[i] = (line[i] + line[i-ch]) & 0xFF
    elif ft == 2:
        for i in range(stride):
            line[i] = (line[i] + prev[i]) & 0xFF
    elif ft == 3:
        for i in range(stride):
            a = line[i-ch] if i >= ch else 0
            line[i] = (line[i] + ((a + prev[i]) >> 1)) & 0xFF
    elif ft == 4:
        for i in range(stride):
            a = line[i-ch] if i >= ch else 0
            b = prev[i]
            c = prev[i-ch] if i >= ch else 0
            pa, pb, pc = abs(b - c), abs(a - c), abs(a + b - 2*c)
            pr = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
            line[i] = (line[i] + pr) & 0xFF
    rows.append(bytes(line))
    prev = line

def px(x, y):
    r = rows[y]
    i = x * ch
    return tuple(r[i:i+3])

for y in (135, 150, 160, 172, 182, 200):
    print(y, [px(x, y) for x in (250, 600, 1100, 1500)])

if out:
    crop = (0, 100, w, 320)
    cw = crop[2] - crop[0]
    chh = crop[3] - crop[1]
    raw2 = b""
    for y in range(crop[1], crop[3]):
        raw2 += b"\x00" + rows[y][crop[0]*ch:crop[2]*ch]
    def chunk(t, b):
        return struct.pack(">I", len(b)) + t + b + struct.pack(">I", zlib.crc32(t + b) & 0xFFFFFFFF)
    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", struct.pack(">IIBBBBB", cw, chh, 8, ct, 0, 0, 0))
    png += chunk(b"IDAT", zlib.compress(raw2, 6))
    png += chunk(b"IEND", b"")
    open(out, "wb").write(png)
    print("wrote", out, cw, chh)
