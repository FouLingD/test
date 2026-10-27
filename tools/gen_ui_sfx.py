"""gen_ui_sfx.py - 生成 UI 音效（历史记录页的"咔"关闭声）

生成的 wav 放到 game/audio/sfx/ 下，由 07_history_fx.rpy 调用。
想调整音色，改下面的参数重跑即可（不需要任何第三方库）。

设计：一个干燥、突兀的"咔"——
  · 3ms 的高通噪声脉冲  → 起音的"啪"
  · 2450Hz 快速衰减正弦 → 塑料/木头的脆
  · 760Hz 中速衰减正弦  → 声音的实体
  · 180Hz 低频短促衰减  → 一点点厚度，避免听起来太薄
"""

import math
import os
import random
import struct
import wave

SR = 44100
DUR = 0.085
PEAK = 0.85

OUT_NAME = "ui_history_close.wav"


def one_pole_lowpass(samples, alpha):
    out = []
    state = 0.0
    for s in samples:
        state += alpha * (s - state)
        out.append(state)
    return out


def main():
    rnd = random.Random(7)
    n = int(SR * DUR)

    white = [rnd.uniform(-1.0, 1.0) for _ in range(n)]

    # 高通 = 原信号 - 一阶低通
    lp = one_pole_lowpass(white, 0.35)
    hp = [white[i] - lp[i] for i in range(n)]

    mix = []
    for i in range(n):
        t = i / SR

        # 噪声脉冲：0.9ms 时间常数，只留起音
        noise_env = math.exp(-t / 0.0009)
        noise = hp[i] * noise_env

        body1 = math.sin(2 * math.pi * 2450 * t) * math.exp(-t / 0.006)
        body2 = math.sin(2 * math.pi * 760 * t) * math.exp(-t / 0.022)
        body3 = math.sin(2 * math.pi * 180 * t) * math.exp(-t / 0.030)

        v = 0.55 * noise + 0.50 * body1 + 0.45 * body2 + 0.30 * body3
        mix.append(v)

    # 0.4ms 起音斜坡，末 4ms 淡出，避免爆音
    attack = int(0.0004 * SR)
    release = int(0.004 * SR)
    for i in range(min(attack, n)):
        mix[i] *= i / attack
    for i in range(release):
        mix[n - 1 - i] *= i / release

    # 去直流 + 归一化
    mean = sum(mix) / n
    mix = [v - mean for v in mix]
    peak = max(abs(v) for v in mix) or 1.0
    scale = PEAK / peak
    mix = [v * scale for v in mix]

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_sfx_tmp")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.normpath(os.path.join(out_dir, OUT_NAME))

    with wave.open(out_path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(b"".join(struct.pack("<h", int(v * 32767)) for v in mix))

    print("wrote", out_path, os.path.getsize(out_path), "bytes")


if __name__ == "__main__":
    main()
