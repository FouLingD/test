"""剪掉音效开头那段听不见的空白（可选加短淡入），输出 48kHz / 单声道 / 16bit WAV。

为什么要这么干：`sfx_page_turn.ogg` 解码后前 40ms 是完全静音，之后 40-140ms
只有满量程 1%-9% 的能量（被 BGM 一盖就听不见），峰值在 308ms。所以"按键到听见"
之间有 100ms 以上是素材自带的，跟引擎延迟无关。

用法（需要 PyAV，见文件末尾注释）：
    python tools/trim_sfx.py <src> <dst> --cut-ms 100 --fade-ms 12

依赖：av（PyAV，wheel 里自带 ffmpeg，能解 Opus）。本机没装 pip 的话：
    python -m pip download av --no-deps -d .whl   # 或直接 urllib 下载 wheel
    解压 wheel 到 .pylibs，然后 PYTHONPATH=.pylibs python tools/trim_sfx.py ...
"""

import argparse
import struct
import wave

from av.audio.resampler import AudioResampler
import av


SR = 48000


def decode_mono16(path):
    """把任意格式解码成 48kHz / 单声道 / 16bit 样本列表。"""

    container = av.open(path)
    stream = container.streams.audio[0]
    resampler = AudioResampler(format="s16", layout="mono", rate=SR)

    chunks = []

    def take(frames):
        for frame in frames:
            chunks.append(bytes(frame.planes[0]))

    for frame in container.decode(stream):
        take(resampler.resample(frame))
    take(resampler.resample(None))

    data = b"".join(chunks)
    return list(struct.unpack("<%dh" % (len(data) // 2), data))


def write_wav(path, samples):
    with wave.open(path, "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(SR)
        f.writeframes(struct.pack("<%dh" % len(samples), *samples))


def trim(samples, cut_ms, fade_ms, tail_trim_ms=0, boost=1.0, boost_ms=0.0):
    start = int(SR * cut_ms / 1000.0)
    end = len(samples) - int(SR * tail_trim_ms / 1000.0)
    out = list(samples[start:end])

    # 开头增益：从 boost 倍线性降到 1 倍，把原本 1%-9% 的"起手"抬到听得见
    ramp = int(SR * boost_ms / 1000.0)
    if boost > 1.0 and ramp > 0:
        for i in range(min(ramp, len(out))):
            gain = 1.0 + (boost - 1.0) * (1.0 - i / float(ramp))
            out[i] = max(-32768, min(32767, int(out[i] * gain)))

    fade = int(SR * fade_ms / 1000.0)
    if fade > 0:
        for i in range(min(fade, len(out))):
            out[i] = int(out[i] * (i / float(fade)))

    # 末尾 3ms 淡出，避免截断爆音
    tail = int(SR * 0.003)
    for i in range(min(tail, len(out))):
        out[-1 - i] = int(out[-1 - i] * (i / float(tail)))
    return out


def report(samples, tag):
    peak = max(abs(x) for x in samples) or 1
    win = int(SR * 0.005)
    rms = []
    for i in range(0, min(len(samples), SR // 4), win):
        chunk = samples[i:i + win]
        rms.append((sum(x * x for x in chunk) / len(chunk)) ** 0.5 / peak)
    first = next((i for i, x in enumerate(samples) if abs(x) > peak * 0.02), 0)
    audible = next((i for i, r in enumerate(rms) if r > 0.10), 0)
    print("%-34s len=%.4fs peak=%5d 2%%@%.1fms audible(>10%%)@%.0fms" % (
        tag, len(samples) / SR, peak, first * 1000.0 / SR, audible * 5))
    print("   rms(5ms):", " ".join("%.2f" % r for r in rms[:30]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--cut-ms", type=float, default=100.0)
    ap.add_argument("--fade-ms", type=float, default=12.0)
    ap.add_argument("--tail-ms", type=float, default=0.0)
    ap.add_argument("--boost", type=float, default=1.0)
    ap.add_argument("--boost-ms", type=float, default=0.0)
    args = ap.parse_args()

    raw = decode_mono16(args.src)
    report(raw, "source")
    out = trim(raw, args.cut_ms, args.fade_ms, args.tail_ms, args.boost, args.boost_ms)
    report(out, "trimmed")
    write_wav(args.dst, out)
    print("wrote", args.dst)


if __name__ == "__main__":
    main()
