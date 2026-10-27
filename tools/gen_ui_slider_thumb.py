"""生成滑块手柄：22x22 的白色正方形，1px 深色描边。

引擎里 Bar 的 thumb 是按 thumb_dim 拉缩绘制的，Solid/Composite 会被压成一条线；
图片（Image）则按自然尺寸绘制，所以这里直接产出一张 PNG 当手柄。

用法：python tools/gen_ui_slider_thumb.py  ->  _sfx_tmp/ui_slider_thumb.png
"""

import os
import struct
import zlib

W = 22
H = 22

WHITE = (255, 255, 255)
INK = (20, 20, 20)


def pixel(x, y):

    edge = x in (0, W - 1) or y in (0, H - 1)

    return INK if edge else WHITE


def write_png(path, width, height):

    raw = bytearray()

    for y in range(height):
        raw.append(0)
        for x in range(width):
            r, g, b = pixel(x, y)
            raw.extend((r, g, b, 255))

    def chunk(tag, data):
        return (
            struct.pack(">I", len(data))
            + tag
            + data
            + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
        )

    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0))
    png += chunk(b"IDAT", zlib.compress(bytes(raw), 9))
    png += chunk(b"IEND", b"")

    with open(path, "wb") as f:
        f.write(png)


if __name__ == "__main__":

    out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_sfx_tmp")
    os.makedirs(out_dir, exist_ok=True)

    out = os.path.join(out_dir, "ui_slider_thumb.png")
    write_png(out, W, H)
    print("wrote", out, os.path.getsize(out), "bytes")
